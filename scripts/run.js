#!/usr/bin/env node
/**
 * Standalone 24h autonomous cycle for Connect AI Lab — 요한계시록 학술 오토메이션 에디션.
 * * [완벽 수정 및 안정화 포인트]:
 * 1. 2, 3권 시작 좌표 미리 기록 (스마트 워프): PDF 파일 이름을 자동 감지하여 1, 2, 3권의 진짜 주석 시작점을 스스로 세팅.
 * 2. max_tokens 한계치 에러 차단: Qwen 모델의 최대 한계인 '4096'으로 고정 최적화.
 * 3. 수석 연구원 영숙이(Youngsuk) 완전 동기화.
 */

const fs = require('fs');
const path = require('path');
const os = require('os');
const axios = require('axios');

let pdfParse;
try {
    const pdfExtract = require('pdf-parse');
    pdfParse = typeof pdfExtract === 'function' ? pdfExtract : pdfExtract.default;
} catch (e) {
    console.error("✗ 'pdf-parse' 패키지가 설치되지 않았습니다. 터미널에 'npm install pdf-parse'를 실행해 주세요.");
    process.exit(1);
}

// ───────────────────────── Config ─────────────────────────
const BRAIN_DIR = 'C:\\AI\\Company-Book';
const LMSTUDIO_URL = 'http://localhost:1234';
const MODEL = 'Qwen/Qwen2.5-7B-Instruct-GGUF';
const TIMEOUT_MS = 3600000;
const PAGES_PER_CYCLE = 5;

// ✨ [여기에 미리 기록해 두었습니다!] 1, 2, 3권의 진짜 주석 시작 페이지 매핑 테이블
const VOLUME_START_PAGES = {
    'vol. 1': 105,
    'vol.1': 105,
    'vol. 2': 54,
    'vol.2': 54,
    'vol. 3': 48,
    'vol.3': 48
};

// ───────────────────────── Helpers ─────────────────────────
const safeRead = (p) => { try { return fs.readFileSync(p, 'utf-8'); } catch { return ''; } };
const today = () => new Date().toISOString().slice(0, 10);
const nowTs = () => new Date().toISOString().replace(/[:.]/g, '-').slice(0, 16);

async function detectEngine() {
    try {
        await axios.get(`${LMSTUDIO_URL}/v1/models`, { timeout: 3000 });
        return { kind: 'lmstudio', url: LMSTUDIO_URL };
    } catch (e) {
        throw new Error(`LM Studio가 응답하지 않습니다. 프로그램이 켜져 있고 [Start Server]가 ON 상태인지 확인해 주세요.`);
    }
}

async function callLLM(engine, system, user) {
    const r = await axios.post(`${engine.url}/v1/chat/completions`, {
        model: MODEL, stream: false, max_tokens: 4096, temperature: 0.3,
        messages: [{ role: 'system', content: system }, { role: 'user', content: user }],
    }, { timeout: TIMEOUT_MS });
    return r.data.choices?.[0]?.message?.content || '';
}

// ───────────────────────── PDF Range Extractor ─────────────────────────
async function extractPdfPageRange(pdfPath, startPage, endPage) {
    const dataBuffer = fs.readFileSync(pdfPath);
    let currentPage = 0;
    const options = {
        pagerender: function (pageData) {
            currentPage++;
            if (currentPage >= startPage && currentPage <= endPage) {
                return pageData.getTextContent().then(function (textContent) {
                    let text = '';
                    for (let item of textContent.items) { text += item.str + ' '; }
                    return text + `\n\n--- [PDF PAGE ${currentPage}] ---\n\n`;
                });
            }
            return Promise.resolve('');
        }
    };
    const parsed = await pdfParse(dataBuffer, options);
    return parsed.text || '';
}

// ───────────────────────── Cycle body ─────────────────────────
async function runCycle() {
    const sharedDir = path.join(BRAIN_DIR, '_shared');
    if (!fs.existsSync(sharedDir)) fs.mkdirSync(sharedDir, { recursive: true });

    const engine = await detectEngine();
    console.log(`✓ 엔진 감지 완료: ${engine.kind} @ ${engine.url} · 모델: ${MODEL}`);

    const criticalDataDir = path.join(BRAIN_DIR, 'Critical_Data');
    if (!fs.existsSync(criticalDataDir)) {
        fs.mkdirSync(criticalDataDir, { recursive: true });
        process.exit(0);
    }

    const files = fs.readdirSync(criticalDataDir);
    const pdfFile = files.find(f => f.toLowerCase().endsWith('.pdf'));

    if (!pdfFile) {
        console.error(`✗ 'Critical_Data' 폴더 내에 요한계시록 주석 PDF 파일이 존재하지 않습니다.`);
        process.exit(1);
    }
    console.log(`✓ 연구 대상 주석서 감지: ${pdfFile}`);

    const targetPdfPath = path.join(criticalDataDir, pdfFile);

    // ✨ 파일 이름 분석 후 시작 페이지 결정 로직
    let defaultStartPage = 105; // 기본값은 1권 기준
    const lowerFileName = pdfFile.toLowerCase();

    for (const [key, page] of Object.entries(VOLUME_START_PAGES)) {
        if (lowerFileName.includes(key)) {
            defaultStartPage = page;
            break;
        }
    }

    const progressFilePath = path.join(sharedDir, 'research_progress.json');
    // 기본 장부 템플릿에 자동 감지된 시작 페이지 적용
    let progress = {
        current_file: pdfFile,
        last_processed_page: defaultStartPage - 1,
        next_page: defaultStartPage
    };

    if (fs.existsSync(progressFilePath)) {
        try {
            const savedProgress = JSON.parse(fs.readFileSync(progressFilePath, 'utf-8'));
            // 만약 동일한 파일이 기존에 진행 중이었다면 이어서 진행
            if (savedProgress.current_file === pdfFile && savedProgress.next_page) {
                progress = savedProgress;
            } else {
                console.log(`📌 새로운 권(Volume) 감지됨: [${pdfFile}] 해당 도서의 기본 주석 시작점(${defaultStartPage}p)으로 자동 세팅합니다.`);
            }
        } catch (e) { }
    }

    const startPage = progress.next_page;
    const endPage = startPage + PAGES_PER_CYCLE - 1;
    console.log(`📚 오늘의 연구 진도 설정: ${startPage}페이지 ~ ${endPage}페이지 (총 ${PAGES_PER_CYCLE}p 독해 시작)`);

    console.log('· 코다리가 PDF 파싱 및 텍스트 청크 변환 작업을 진행 중...');
    const todaysRawText = await extractPdfPageRange(targetPdfPath, startPage, endPage);

    if (!todaysRawText.trim() || todaysRawText.length < 100) {
        console.log(`🏁 주석서의 끝에 도달했거나 읽을 수 있는 텍스트가 없습니다. 연구 사이클을 종료합니다.`);
        process.exit(0);
    }

    const identityConfig = safeRead(path.join(sharedDir, 'identity.md'));
    const decisions = safeRead(path.join(sharedDir, 'decisions.md')).slice(-3000);

    const sysPrompt = `당신은 요한계시록 학술 연구 자동화 연구소(Company-Book)의 수석 조율관입니다.
배속된 세 명의 AI 연구원(레오, 현빈, 영숙)의 지침과 정체성을 엄격히 준수하여 최종 리포트를 도출하세요.

${identityConfig ? `[배속 에이전트 및 운영 지침]\n${identityConfig}` : '[주의]: identity.md 파일이 비어있습니다. 기본 학술 비평 모드로 작동합니다.'}

[이전 연구 컨텍스트 및 누적 내역]
${decisions || '최초의 연구 사이클입니다.'}

[오늘의 핵심 임무]
1. 제공된 주석서 원문(${startPage}p~${endPage}p)을 바탕으로 요한계시록 장-절별 매트릭스를 구성하세요.
2. 레오의 임무에 따라 교회사 속 '4대 패러다임(과거주의, 역사주의, 미래주의, 상징주의)' 관점을 철학적·시스템적으로 촘큼하게 분리하여 작성하세요.
3. 현빈의 임무에 따라 사이비·이단 교파들의 왜곡된 노이즈 해석(비유 풀이, 공포 마케팅)을 정통 비평학과 대조하여 날카롭게 걸러내고 비평 탭에 고발하세요.
4. 영숙이(Youngsuk)의 임무에 따라 최종 산출물이 책의 정식 챕터(Chapter)로 즉시 들어갈 수 있도록 가독성이 극대화된 '구절별 해석사 비교 매트릭스(테이블)'와 깊이 있는 '학술 요약문' 형태로 문장을 조립하세요. 잡설은 배제하고 scannable한 학술서 톤을 유지하세요.`;

    const userMsg = `## 오늘의 연구 대상 주석 원문 (${pdfFile} - ${startPage}p~${endPage}p)
${todaysRawText}

위의 5페이지 분량을 정독하고, 배속된 세 연구원(레오, 현빈, 영숙)의 정체성이 100% 녹아든 백과사전식 4대 패러다임 리포트를 마크다운으로 출력해 주세요.`;

    console.log('· 에이전트 협업 연구 진행 중 (로컬 LLM 연산)... 오래 걸릴 수 있으니 창을 닫지 마세요.');
    const out = await callLLM(engine, system = sysPrompt, user = userMsg);
    if (!out.trim()) throw new Error('에이전트가 리포트 생성에 실패했습니다. (답변이 비어있음)');

    const sessionDir = path.join(BRAIN_DIR, 'sessions');
    if (!fs.existsSync(sessionDir)) fs.mkdirSync(sessionDir, { recursive: true });
    fs.writeFileSync(path.join(sessionDir, `page_${startPage}-${endPage}_report.md`), out);

    const convDir = path.join(BRAIN_DIR, '00_Raw', 'conversations');
    fs.mkdirSync(convDir, { recursive: true });
    const dayFile = path.join(convDir, `${today()}.md`);
    if (!fs.existsSync(dayFile)) {
        fs.writeFileSync(dayFile, `# 📜 ${today()} 요한계시록 학술 연구 대화록\n`);
    }
    const ts = new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false });
    const block = `\n## [${ts}] 🌙 **일일 5페이지 자동화 연구 사이클** (${startPage}p~${endPage}p)\n\n${out}\n`;
    fs.appendFileSync(dayFile, block);

    progress.current_file = pdfFile;
    progress.last_processed_page = endPage;
    progress.next_page = endPage + 1;
    fs.writeFileSync(progressFilePath, JSON.stringify(progress, null, 2));

    console.log(`✓ 사이클 완료! 산출물이 저장되었습니다: ${sessionDir}/page_${startPage}-${endPage}_report.md`);
    console.log(`✓ 진도 장부 업데이트: 다음엔 ${progress.next_page}페이지부터 가동됩니다.`);
}

runCycle().catch((e) => {
    console.error('✗ 사이클 구동 실패:', e.message);
    process.exit(1);
});