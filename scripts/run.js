#!/usr/bin/env node
/**
 * Antigravity Advanced Loop Engine for Connect AI Lab
 * [구글 정식 @google/genai 라이브러리 탑재 + gemini-2.5-flash 엔진 + 5단계 순차 루프 + 503 과부하 방지 슬립 장치]
 */

const fs = require('fs');
const path = require('path');
const { GoogleGenAI } = require('@google/genai');

const BRAIN_DIR = 'C:\\AI\\Company-Book';
const GEMINI_API_KEY = 'AIzaSyDTnAlJ81ZW5MZQQpo_bbiUjvEquaV6M5Y';

// 구글 순정 라이브러리 초기화 (주소창 매핑 에러율 0%)
const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY });

const safeRead = (p) => { try { return fs.readFileSync(p, 'utf-8'); } catch { return ''; } };
const today = () => new Date().toISOString().slice(0, 10);

// 구글 서버 트래픽 제한(503)을 우회하기 위한 밀리초 단위 대기 함수
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

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

    console.log(`🚀 [안티그래비티 순정 루프 오토메이션 가동] 대상 구역: [${rangeStr}]`);

    const sharedDir = path.join(BRAIN_DIR, '_shared');
    const identityConfig = safeRead(path.join(sharedDir, 'identity.md'));
    const decisions = safeRead(path.join(sharedDir, 'decisions.md')).slice(-3000);

    // 역할별 순차 루프 제어 배열
    const roles = [
        { id: 1, name: "■ 역할 1번 (What 요원)", task: "텍스트 전승 환경 및 3대 구절별 실제 대상, 인물명, 조직명 상세 데이터 세트 서술형 매핑" },
        { id: 2, name: "■ 역할 2번 (Mechanism 요원)", task: "주체별 해석 알고리즘 심층 해부 및 현대 실상론의 사후 역산 매칭 회로 단계별 줄글 서술" },
        { id: 3, name: "■ 역할 3번 (Context 요원)", task: "1C, 5C, 16C, 19C, 21C 한국 장막성전 하위문화 등 5대 축의 완전한 수평 비교 대형 표(Table) 서술" },
        { id: 4, name: "■ 역할 4번 (Archiver 요원)", task: "앞서 도출된 데이터를 바탕으로 구절별로 완벽하게 제련된 평면적 지식 통합 마크다운 단락 기술" },
        { id: 5, name: "■ 역할 5번 (Publisher 요원)", task: "출간용 다차원 프리미엄 매트릭스 테이블 칸 채우기 및 3대 학술 함수에 대한 에세이 형태의 긴 서술" }
    ];

    let accumulatedReport = "";

    // 1번부터 5번까지 구글 서버에 알아서 순차적으로 연산을 이어 달리기 (총 5개 세션 루프)
    for (const role of roles) {
        // 구글 트래픽 엔진을 속이기 위해 스텝 2번부터는 요청 직전 8초간 안전 휴식 가동
        if (role.id > 1) {
            console.log(`· 구글 클라우드 트래픽 보호 정지 중... (8초 후 ${role.id}번 요원 자동 출격)`);
            await sleep(8000);
        }

        console.log(`\n· [스텝 ${role.id}/5] ${role.name} 가동 중... (분량 눈치 없이 초고밀도 집필 중)`);

        const systemInstruction = `${identityConfig}\n\n[이전 연구 자산]\n${decisions}\n\n당신은 현재 위 지침 중 오직 [${role.name}]의 임무만 독점적으로 수행해야 합니다. 절대로 요약하지 말고 단행본 책의 한 페이지를 채우듯이 아주 길고 장황한 서술형 문장으로만 작성하세요. 주관적 비평어는 절대 금지합니다.`;

        const prompt = `[원본 분석 데이터]\n${rawContent}\n\n[현재까지 작성된 앞 단계 보고서]\n${accumulatedReport}\n\n지침에 따라 이번 단계인 [${role.name}: ${role.task}] 내용을 이전 단계 내용과 이어지도록 아주 자세하게 서술형 줄글로 작성해 주세요.`;

        try {
            const response = await ai.models.generateContent({
                model: 'gemini-2.5-flash',
                contents: prompt,
                config: {
                    systemInstruction: systemInstruction,
                    temperature: 0.2,
                    maxOutputTokens: 8192 // 각 역할마다 글자 수 맥시멈 제한 해제
                }
            });

            const blockResult = response.text || '';
            accumulatedReport += `\n\n### ${role.name}\n${blockResult}`;
            console.log(`✓ [스텝 ${role.id}/5 완료] 데이터 확보 성공.`);
        } catch (err) {
            console.error(`✗ [스텝 ${role.id} 에러 발생]:`, err.message);
            process.exit(1);
        }
    }

    // 최종 파일 마스터피스 조립 및 강제 락인 마감
    try {
        const verseClean = rangeStr.replace(/analysis_/g, '').replace(/_/g, ' ');
        const frontmatter = `---\nverse: "${verseClean}"\nera: ["1st-Century", "Patristic", "Medieval", "Reformation", "Modern", "21st-Century"]\nscholars: ["Aune", "Origen", "Augustine", "Joachim", "Luther", "Grotius", "Darby", "Shincheonji"]\nkeywords: ["Historical Anchor", "Genre Convention", "Allegory", "No-Evaluation-v5"]\n---\n\n## ANTIGRAVITY INTEGRATED COORDINATION REPORT — REV-HISTORICAL-DATA-INTEGRATION\n\n본 보고서는 제공된 데이터 기반으로 요한계시록의 1세기 역사학적 고증과 이후 2,000년간 발생한 주요 해석 데이터 세트를 수평적으로 구조화하고 대조한 정밀 상세 기술서입니다.`;

        const fixedPhrase = `\n\n---\n> 📝 *이 내용의 통찰은 책 《사기쳐줘서 고마워》 내용을 통해 정리하였습니다.*`;
        const finalMasterpiece = frontmatter + accumulatedReport + fixedPhrase + `\n\n"본 보고서는 요한계시록의 주요 구절에 대한 시대별·주체별 해석 데이터를 수평선상에 나열하여 각각의 객관적 해석 메커니즘을 상호 비교하고, 이를 하나의 다차원적 해석학 지식 체계로 통합하며 분석을 마감함."`;

        const sessionDir = path.join(BRAIN_DIR, 'sessions');
        if (!fs.existsSync(sessionDir)) fs.mkdirSync(sessionDir, { recursive: true });
        const fileName = `analysis_${rangeStr.replace(/\s+/g, '_')}.md`;

        fs.writeFileSync(path.join(sessionDir, fileName), finalMasterpiece, 'utf8');
        console.log(`\n🏆 [자산 공장 완공] sessions/${fileName} 에 단행본급 원고 자동 박제 완료!`);

        const masterIndexPath = path.join(BRAIN_DIR, 'MASTER_INDEX.md');
        fs.appendFileSync(masterIndexPath, `- [${today()}] 요한계시록 5인 순차 오토메이션 융합 리포트 (${rangeStr}) ➔ [[sessions/${fileName}]]\n`);

        // 깃허브 원격 요새 백업 프로세스
        try {
            const { execSync } = require('child_process');
            console.log('· [원격 백업] 깃허브 요새로 무결점 자산 업로드 중...');
            execSync('git add .', { cwd: BRAIN_DIR });
            execSync(`git commit -m "Antigravity-Watcher: ${rangeStr} v5 loop perfect auto"`, { cwd: BRAIN_DIR });
            execSync('git push origin main', { cwd: BRAIN_DIR });
            console.log(`🚀 [자동화 공정 전체 완료] 원격 요새 반영까지 원터치 성공!`);
        } catch (gitErr) {
            console.log(`⚠️ 깃허브 백업 보류 (원고 자산은 로컬에 완벽하게 세이브됨)`);
        }
    } catch (e) {
        console.error('✗ 최종 조립 및 파일 저장 실패:', e.message);
    }
}

run();