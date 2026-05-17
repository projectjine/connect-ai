#!/usr/bin/env node
/**
 * Antigravity Ultra-Density 9-Segregation Engine - Final Master
 * [공정 체인 9단계 최종 세분화 + 외부 key.txt 로드 + 성경 문장 원형 강제 주입]
 */

const fs = require('fs');
const path = require('path');
const { GoogleGenAI } = require('@google/genai');

const BRAIN_DIR = 'C:\\AI\\Company-Book';

const safeRead = (p) => { try { return fs.readFileSync(p, 'utf-8'); } catch { return ''; } };
const today = () => new Date().toISOString().slice(0, 10);
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const sharedDir = path.join(BRAIN_DIR, '_shared');
const GEMINI_API_KEY = safeRead(path.join(sharedDir, 'key.txt')).trim();

if (!GEMINI_API_KEY) {
    console.error(`\n✗ 에러: _shared/key.txt 파일에 새로운 API 키가 입력되지 않았거나 파일을 찾을 수 없습니다!`);
    process.exit(1);
}

const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY });

function fetchLocalRawFile() {
    const inputDir = path.join(BRAIN_DIR, 'raw_inputs');
    const files = fs.readdirSync(inputDir).filter(f => f.endsWith('.txt') || f.endsWith('.md'));
    if (files.length === 0) throw new Error(`⚠️ raw_inputs 폴더 안에 분석할 원고 파일이 없습니다!`);
    return fs.readFileSync(path.join(inputDir, files[0]), 'utf-8').trim();
}

async function run() {
    const rawContent = fetchLocalRawFile();
    if (rawContent.length < 20) process.exit(0);

    const rangeMatch = rawContent.match(/범위:\s*([^\n\r]+)/) || ["", "연구 대상 구역"];
    const rangeStr = rangeMatch[1].trim().replace(/[:/\\*?|<>=]/g, '');

    console.log(`🚀 [안티그래비티 9단계 풀-체인 분절 오토메이션 가동] 대상 구역: [${rangeStr}]`);

    const decisions = safeRead(path.join(sharedDir, 'decisions.md')).slice(-3000);

    const targetVerses = `
★ [반드시 본문에 원형 그대로 기재해야 하는 3대 고정 구절 문장 원형]
- [구절 1] 요한계시록 1장 20절 "네가 본 것은 내 오른손의 일곱 별의 비밀과 또 일곱 금 촛대라"
- [구절 2] 요한계시록 2장 17절 "이기는 그에게는 내가 감추었던 만나를 주고 또 흰 돌을 줄 터인데"
- [구절 3] 요한계시록 13장 18절 "지혜가 여기 있으니 총명한 자는 그 짐승의 수를 세어 보라 그것은 사람의 수니 그의 수는 육백육십육이니라"
`;

    // 9단계 초정밀 공정 파이프라인 레이아웃
    const roles = [
        { id: 1, name: "■ 역할 1번 (What 요원)", file: "identity_1.md", header: "### ■ 역할 1번 (What 요원)" },
        { id: 2, name: "■ 역할 2번 (Mechanism 요원)", file: "identity_2.md", header: "### ■ 역할 2번 (Mechanism 요원)" },
        { id: 3, name: "■ 역할 3번 (Context 요원)", file: "identity_3.md", header: "### ■ 역할 3번 (Context 요원)" },
        { id: 41, name: "■ 역할 4-1번 (일곱 별 아카이버)", file: "identity_4_1.md", header: "### ■ 역할 4번 (Archiver 요원) - 구절 1 통합" },
        { id: 42, name: "■ 역할 4-2번 (흰 돌 아카이버)", file: "identity_4_2.md", header: "## 구절 2 통합" },
        { id: 43, name: "■ 역할 4-3번 (666 아카이버)", file: "identity_4_3.md", header: "## 구절 3 통합" },
        { id: 51, name: "■ 역할 5-1번 (일곱 별 퍼블리셔)", file: "identity_5_1.md", header: "### ■ 역할 5번 (Publisher 요원) - 대조 매트릭스 [구절 1]" },
        { id: 52, name: "■ 역할 5-2번 (흰 돌 퍼블리셔)", file: "identity_5_2.md", header: "## 대조 매트릭스 [구절 2]" },
        { id: 53, name: "■ 역할 5-3번 (666 퍼블리셔 및 마감)", file: "identity_5_3.md", header: "## 대조 매트릭스 [구절 3] 및 최종 함수 정리" }
    ];

    let accumulatedReport = "";
    let idx = 1;

    for (const role of roles) {
        if (idx > 1) {
            console.log(`· 503 과부하 방지 안전 대기 중... (8초 후 ${role.name} 세션 출격)`);
            await sleep(8000);
        }

        console.log(`\n· [스텝 ${idx}/9] ${role.name} 독립 연산 가동...`);

        const roleSpecificIdentity = safeRead(path.join(sharedDir, role.file));
        if (!roleSpecificIdentity) {
            console.error(`✗ 에러: ${role.file} 지침서 파일이 존재하지 않습니다!`);
            process.exit(1);
        }

        const systemInstruction = `${roleSpecificIdentity}\n\n[이전 연구 자산]\n${decisions}\n\n주의: 당신은 오직 이 분절된 지침서에 명시된 임무만 독점 수행하며, 출력 한계선 눈치 보지 말고 최고 밀도로 쏟아내십시오.`;
        const prompt = `${targetVerses}\n\n[원본 분석 데이터]\n${rawContent}\n\n위의 3대 고정 구절과 문장 원형을 생략 없이 그대로 기재하고, 지침에 따라 오직 당신에게 할당된 독립 임무에만 100% 집중하여 팩트 결과만 정밀하게 정리해 주세요. 지정된 양식(표 등)이 있다면 절대로 자르지 말고 끝까지 채워 출력하세요.`;

        try {
            const response = await ai.models.generateContent({
                model: 'gemini-2.5-flash',
                contents: prompt,
                config: {
                    systemInstruction: systemInstruction,
                    temperature: 0.2,
                    maxOutputTokens: 8192
                }
            });

            const blockResult = response.text || '';
            accumulatedReport += `\n\n${role.header}\n${blockResult}`;
            console.log(`✓ [스텝 ${idx}/9 완료] ${role.name} 데이터 완벽 확보.`);
            idx++;
        } catch (err) {
            console.error(`✗ [스텝 ${role.name} 실패]:`, err.message);
            process.exit(1);
        }
    }

    try {
        const verseClean = rangeStr.replace(/analysis_/g, '').replace(/_/g, ' ');
        const frontmatter = `---\nverse: "${verseClean}"\nera: ["1st-Century", "Patristic", "Medieval", "Reformation", "Modern", "21st-Century"]\nscholars: ["Aune", "Origen", "Augustine", "Joachim", "Luther", "Grotius", "Darby", "Shincheonji"]\nkeywords: ["Horizontal Anchor", "Absolute-Text", "9-Segregation-Perfect"]\n---\n\n## ANTIGRAVITY INTEGRATED COORDINATION REPORT — REV-HISTORICAL-DATA-INTEGRATION\n\n본 보고서는 제공된 데이터 기반으로 요한계시록의 1세기 역사학적 고증과 이후 2,000년간 발생한 주요 해석 데이터 세트를 수평적으로 구조화하고 대조한 정밀 상세 기술서입니다.`;

        const fixedPhrase = `\n\n---\n> 📝 *이 내용의 통찰은 책 《사기쳐줘서 고마워》 내용을 통해 정리하였습니다.*`;
        const finalMasterpiece = frontmatter + accumulatedReport + fixedPhrase + `\n\n"본 보고서는 요한계시록의 주요 구절에 대한 시대별·주체별 해석 데이터를 수평선상에 나열하여 각각의 객관적 해석 메커니즘을 상호 비교하고, 이를 하나의 다차원적 해석학 지식 체계로 통합하며 분석을 마감함."`;

        const sessionDir = path.join(BRAIN_DIR, 'sessions');
        if (!fs.existsSync(sessionDir)) fs.mkdirSync(sessionDir, { recursive: true });
        const fileName = `analysis_${rangeStr.replace(/\s+/g, '_')}.md`;

        fs.writeFileSync(path.join(sessionDir, fileName), finalMasterpiece, 'utf8');
        console.log(`\n🏆 [9단계 오토메이션 마스터피스 조립 완공] sessions/${fileName} 저장 완료!`);

        const masterIndexPath = path.join(BRAIN_DIR, 'MASTER_INDEX.md');
        fs.appendFileSync(masterIndexPath, `- [${today()}] 요한계시록 9단계 극초밀도 개별 분절 리포트 (${rangeStr}) ➔ [[sessions/${fileName}]]\n`);

        try {
            const { execSync } = require('child_process');
            console.log('· [원격 요새 백업] 깃허브 업로드 중...');
            execSync('git add .', { cwd: BRAIN_DIR });
            execSync(`git commit -m "Antigravity-Watcher: ${rangeStr} v7 9-chain loop perfect"`, { cwd: BRAIN_DIR });
            execSync('git push origin main', { cwd: BRAIN_DIR });
            console.log(`🚀 [자동화 공정 전체 완료] 최종 완결본 원터치 백업 성공!`);
        } catch (gitErr) {
            console.log(`⚠️ 깃허브 백업 보류 (원고 자산은 로컬에 세이브됨)`);
        }
    } catch (e) {
        console.error('✗ 최종 조립 실패:', e.message);
    }
}

run();