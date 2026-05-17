#!/usr/bin/env node
/**
 * Advanced Hybrid Intel Engine for Connect AI Lab — 요한계시록 학술 오토메이션
 * [5인 체제 + 100% 로컬 파일 직접 흡수 + 구글 API 완전 박멸 최종형]
 */

const fs = require('fs');
const path = require('path');
const axios = require('axios');

// ───────────────────────── Config ─────────────────────────
const BRAIN_DIR = 'C:\\AI\\Company-Book';
const MODEL = 'Qwen/Qwen2.5-7B-Instruct-GGUF';
const TIMEOUT_MS = 3600000;

const safeRead = (p) => { try { return fs.readFileSync(p, 'utf-8'); } catch { return ''; } };
const today = () => new Date().toISOString().slice(0, 10);

async function detectEngine() {
    const ports = [1234, 1235];
    for (const port of ports) {
        const url = `http://localhost:${port}`;
        try {
            await axios.get(`${url}/v1/models`, { timeout: 2000 });
            return { kind: 'lmstudio', url: url };
        } catch (e) { }
    }
    throw new Error(`LM Studio 서버가 꺼져있습니다. 프로그램을 켜고 [Start Server]를 눌러주세요.`);
}

// 📦 로컬 지정 폴더에서 다운로드된 원료 파일을 직접 흡수하는 안전 로직
function fetchLocalRawFile() {
    const inputDir = path.join(BRAIN_DIR, 'raw_inputs');

    // 폴더가 없으면 자동 생성
    if (!fs.existsSync(inputDir)) {
        fs.mkdirSync(inputDir, { recursive: true });
    }

    // 폴더 내에 읽을 수 있는 텍스트/마크다운 파일 탐색
    const files = fs.readdirSync(inputDir).filter(f => f.endsWith('.txt') || f.endsWith('.md'));

    if (files.length === 0) {
        throw new Error(`⚠️ raw_inputs 폴더(${inputDir}) 안에 분석할 원고 파일(.txt 또는 .md)이 없습니다! 파일을 넣어주세요.`);
    }

    // 가장 첫 번째 파일을 원료로 채택
    const targetPath = path.join(inputDir, files[0]);
    console.log(`📦 로컬 요새 내부 [raw_inputs/${files[0]}] 원료 다이렉트 수집 완료.`);
    return fs.readFileSync(targetPath, 'utf-8').trim();
}

async function callLLM(engine, system, user) {
    const r = await axios.post(`${engine.url}/v1/chat/completions`, {
        model: MODEL, stream: false, max_tokens: 8192, temperature: 0.3,
        messages: [{ role: 'system', content: system }, { role: 'user', content: user }],
    }, { timeout: TIMEOUT_MS });
    return r.data.choices?.[0]?.message?.content || '';
}

// ───────────────────────── Main Run ─────────────────────────
async function run() {
    const engine = await detectEngine();

    // 구글 통신망을 거치지 않고 내 컴퓨터 폴더에서 직접 텍스트 로드
    const rawContent = fetchLocalRawFile();

    if (rawContent.length < 20) {
        console.log(`⚠️ 원료 파일의 내용이 너무 짧거나 비어있습니다.`);
        process.exit(0);
    }

    const rangeMatch = rawContent.match(/범위:\s*([^\n]+)/) || ["", "연구 대상 구역"];
    const rangeStr = rangeMatch[1].trim().replace(/[:/\\*?|<>=]/g, '');

    console.log(`🚀 안티그래비티 5인 마스터 로컬 연산 가동! 대상 구역: [${rangeStr}]`);

    const sharedDir = path.join(BRAIN_DIR, '_shared');
    const identityConfig = safeRead(path.join(sharedDir, 'identity.md'));
    const decisions = safeRead(path.join(sharedDir, 'decisions.md')).slice(-3000);

    const sysPrompt = `당신은 요한계시록 2,000년 해석사를 '1세기 역사학적 사실(Historical Anchor)' 중심으로 구조화하는 안티그래비티(Antigravity) 통합 조율 시스템입니다.
모든 요원은 주관적 비난, 감정적 수사학, 종교적 편향성을 철저히 필터링하고, 법의학 보고서 수준의 차갑고 건조한 '사실주의(Objectivity) 톤앤매너'를 100% 유지하세요.

${identityConfig ? `[배속 에이전트 및 운영 지침]\n${identityConfig}` : ''}
[이전 연구 컨텍스트] ${decisions || '최초의 연구 사이클입니다.'}

제공된 로컬 파일 내부의 통합 로우 데이터를 바탕으로, 각 요원은 자신의 엄격한 경계선 안에서만 연산한 뒤 이를 최종 결합하세요.

■ 역할 1번 (What 요원): 팩트 및 키워드 추출
■ 역할 2번 (Mechanism 요원): 내재적 논리 공식 규명
■ 역할 3번 (Context 요원): 외재적 콘텍스트 환경 규명
■ 역할 4번 (Archiver 요원): 취합 및 옵시디언 프론트매터 아카이빙
■ 역할 5번 (Publisher 요원): 1단계 비즈니스 가치 창출 및 최종 마감

[출력 프로토콜]: 반드시 상기 5개 역할의 결과물이 순서대로 단 하나의 완성형 문서로 누락 없이 표현되도록 설계하여 반환하세요.`;

    console.log('· 안티그래비티 5인 팀이 고밀도 지식 융합 연산 중...');
    const llmOut = await callLLM(engine, sysPrompt, rawContent);

    if (!llmOut.trim()) throw new Error('리포트 생성 실패');

    console.log('· 역할 4번/5번 시스템 결합 중...');
    const verseClean = rangeStr.replace(/analysis_/g, '').replace(/_/g, ' ');

    const frontmatter = `---
verse: "${verseClean}"
era: ["1st-Century", "Patristic", "Medieval", "Reformation", "Modern", "21st-Century"]
scholars: ["Aune", "Origen", "Augustine", "Joachim", "Luther", "Grotius", "Darby", "Shincheonji"]
keywords: ["Historical Anchor", "Genre Convention", "Allegory", "Historicist Error", "Business-Asset-v1"]
---

`;

    const fixedPhrase = `

---

> 📝 *이 내용의 통찰은 책 《사기쳐줘서 고마워》 내용을 통해 정리하였습니다.*`;

    const finalMasterpiece = frontmatter + llmOut + fixedPhrase;

    const sessionDir = path.join(BRAIN_DIR, 'sessions');
    if (!fs.existsSync(sessionDir)) fs.mkdirSync(sessionDir, { recursive: true });
    const fileName = `analysis_${rangeStr.replace(/\s+/g, '_')}.md`;
    fs.writeFileSync(path.join(sessionDir, fileName), finalMasterpiece, 'utf8');
    console.log(`✓ [자산 박제 완료] sessions/${fileName}`);

    const masterIndexPath = path.join(BRAIN_DIR, 'MASTER_INDEX.md');
    const indexLine = `- [${today()}] 요한계시록 5인 통합 객관화 리포트 (${rangeStr}) ➔ [[sessions/${fileName}]]\n`;
    fs.appendFileSync(masterIndexPath, indexLine);
    console.log(`✓ [마스터 인덱스] MASTER_INDEX.md 자동 갱신 완료.`);

    console.log(`✓ 로컬 백업 및 마스터 인덱스 색인이 성공적으로 완수되었습니다.`);

    // GitHub 자동 백업
    try {
        const { execSync } = require('child_process');
        console.log('· [깃허브 백업] 원격 요새로 업로드 중...');
        execSync('git add .', { cwd: BRAIN_DIR });
        execSync(`git commit -m "Antigravity-Watcher: ${rangeStr} objective report master"`, { cwd: BRAIN_DIR });
        execSync('git push origin main', { cwd: BRAIN_DIR });
        console.log(`🚀 [깃허브 백업 성공] 원격 요새 보존 완료!`);
    } catch (e) {
        console.log(`⚠️ 깃허브 백업 보류:`, e.message);
    }
}

run().catch(e => console.error('✗ 구동 실패:', e.message));