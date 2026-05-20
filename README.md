<p align="center">
  <img src="assets/icon.png" width="120" alt="Connect AI Logo" />
</p>

<h1 align="center">Connect AI v2 (P-Reinforce)</h1>

<p align="center">
  <strong>100% Local · 100% Offline · Autonomous Knowledge Engine</strong><br/>
  VS Code / Cursor 확장 프로그램으로, 당신의 낡은 IDE를 최상위 에이전트 대학(A.U)의 심장으로 진화시킵니다.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2.1.30-blue" alt="version" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license" />
  <img src="https://img.shields.io/badge/integration-Agent_University-purple" alt="integration" />
  <img src="https://img.shields.io/badge/engine-Ollama%20%7C%20LM%20Studio-orange" alt="engine" />
</p>

---

## 🌟 Overview: Intellectual Authority Engine
Connect AI는 단순한 코딩 에이전트를 넘어, **지적 권위 1인 기업**을 위한 완벽한 지식 생산 엔진입니다.
**P-Reinforce 아키텍처**를 기반으로, 사용자의 철학적 영감을 **S등급 학술 데이터**와 융합하여 독보적인 콘텐츠를 자율적으로 생산합니다.

### 🧠 핵심 시스템: 5단계 지식 퍼널 (Knowledge Funnel)
에이전트는 모든 지식을 5단계 깊이로 체계화하여 관리합니다:
1. **Lv.1 (SNS)**: 직관적 후킹 및 페인 포인트 자극
2. **Lv.2 (Blog)**: 과학/통계 근거 기반 객관적 현상 해설
3. **Lv.3 (Member)**: 구조화된 지식 지도 및 핵심 요약
4. **Lv.4 (Premium)**: 최신 학술 논문 및 작가 철학 융합 (《사기쳐 줘서 고마워》 기반)
5. **Lv.5 (Solution)**: 실천 가이드 및 워크북

---

## 👥 Core Agents (전담 에이전트 팀)

### 1. 코다리 (Kodari) — Content Editor
5단계 퍼널과 학술 데이터 등급(S/A/B)을 엄격히 준수하며 "사실 기반의 철학적 글쓰기"를 수행합니다. AGO/GEO/CEO 최적화를 통해 당신의 지적 권위를 검색 엔진 상단에 배치합니다.

### 2. 비주얼 마스터 (Visual Master) — Art Director
코다리의 텍스트를 시각적 언어로 번역합니다. 고전 명화를 현대적으로 재해석하며, 브랜드 메인 컬러인 **Soft Sage (#D4E2D4)**를 활용하여 우아하고 독보적인 비주얼 시스템을 구축합니다.

---

## ⚡ Core Features

### 1. 🧠 Agent University (A.U) 완벽 연동
Agent University 웹 플랫폼과 실시간으로 통신합니다. 
웹에서 버튼 한 번 누르는 즉시, 로컬 VS Code의 `4825` 포트를 통해 프리미엄 브레인 팩(Premium Brain Pack) 지식이 로컬 인공지능 뇌(`~/.connect-ai-brain`)에 자동 주입되어 신경망을 확장합니다.

### 2. 📂 자율 지식 구조화 (Zero-Interaction Styling)
유저가 던져주는 원시 데이터(Raw Data)를 에이전트가 스스로 판단해 `10_Wiki`, `00_Raw`, `🚀 Skills` 와 같은 완벽한 P-Reinforce 템플릿 규격의 Markdown 파일로 분할-조립하여 저장합니다.

### 3. ☁️ 클라우드 동기화 (Auto-Git Sync 100%)
로컬 PC에서 파일 생성이 일어나는 순간, 에이전트가 스스로 GitHub 저장소에 `git add`, `commit`, `push`를 수행합니다. 
마스터는 이제 지루한 푸시 커맨드를 입력할 필요가 없습니다.

### 4. 🔗 설치형 모델 자동 감지 (Dynamic Model Detection)
Ollama 또는 LM Studio에 설치된 모델을 내부 API(`v1/models`)를 호출하여 자동 감지하고, UI의 스위치 보드(드롭다운)에 연결합니다. 어떤 모델을 쓸지 번거롭게 입력하지 마십시오.

---

## ⚒️ Agent Capabilities (에이전트 권한)

로컬 머신의 파일 시스템과 터미널에 대한 통제권을 인공지능에게 부여합니다. (100% 안전한 권한 승인 기반)

| Action | Description |
|:--|:--|
| **📄 Create Files** | 새로운 파일과 폴더를 생성합니다 |
| **✏️ Edit Files** | 기존 파일 내의 코드를 수정합니다 |
| **🗑️ Delete Files** | 불필요한 파일을 즉각 파쇄합니다 |
| **📖 Read Files** | 마스터의 프로젝트 파일을 읽어 맥락을 파악합니다 |
| **📂 Browse Directories** | 디렉토리 구조를 분석합니다 |
| **🖥️ Run Commands** | `npm run build`, `git push` 등 터미널 명령을 수행합니다 |

---

## 📥 Installation (설치 방법)

### A.U 멤버십 유저 (Recommended)
1. 상단 탭의 [Releases](https://github.com/wonseokjung/connect-ai/releases) 메뉴로 진입.
2. 최신 `v2.1.30.vsix` 파일을 다운로드.
3. VS Code 에서 `Cmd+Shift+P` → **Extensions: Install from VSIX** → 다운받은 파일 선택

### 개발자 빌드 (Build from Source)
```bash
git clone https://github.com/wonseokjung/connect-ai.git
cd connect-ai
npm install
npm run compile
npx vsce package
```

---

## ⚙️ Engine Setup (엔진 설정 방법)

### ✅ LM Studio (Apple Silicon, Windows) - 권장
1. [lmstudio.ai](https://lmstudio.ai/) 에서 설치
2. Gemma 3, Llama 3 또는 Qwen Coder 등 원하는 모델 로드
3. **Developer 탭(좌측 `<>` 메뉴)** 진입 후 **Start Server** 클릭
4. Connect AI의 ⚙️ 채팅방 설정에서 엔진을 "LM Studio"로 선택 (자동 모델 인덱싱 완료)

### ✅ Ollama (Mac, Linux)
```bash
brew install ollama
ollama pull gemma3   # 원하는 모델 풀링
```
Connect AI에서 설정만 "Ollama"로 바꿔주시면 끝납니다.

---

## 🔒 Privacy (완벽한 보안)

- **Zero Cloud API:** 당신의 코드는 외부 클라우드 통신망을 타지 않습니다.
- **Zero Telemetry:** 모든 연산력은 100% Local Inference 환경에서 이루어집니다.
- 기업 보안 등급에 준하는 극강의 밀폐형 로컬 지식망 생성을 보장합니다.

---

<p align="center">
  <strong>Built for Antigravity & Agent University</strong><br/>
  Designed by <a href="https://github.com/wonseokjung">Jay</a> × Connect AI Architect
</p>
