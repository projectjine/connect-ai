import os
import requests
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

def publish_post(title, content, status='draft'):
    endpoint = f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts"
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
    payload = {"title": title, "content": content, "status": status}
    
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"[OK] Success: Post '{title}' published.")
        print(f"Link: {response.json().get('link')}")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")

title = "[학술 분류: Neuroscience] 고립은 비유가 아니다: 당신의 뇌가 느끼는 ‘물리적 통증’의 실체"
content = """
<p><strong>[학술 분류]</strong> Life Sciences & Medicine (Neuroscience)</p>

<hr />

<h2>"외로움은 감정이 아니라, 생물학적 비명이다"</h2>

<p>우리는 흔히 고립감을 느낄 때 "마음이 찢어진다"거나 "가슴이 아프다"는 표현을 씁니다. 지금까지 인문학은 이를 아름다운 비유로 다루어 왔지만, 현대 신경과학의 결론은 훨씬 더 차갑고 명확합니다.</p>

<h3>1. 팩트 체크: dACC와 전방 뇌섬엽의 비밀</h3>
<p>인간의 뇌에서 사회적 소외와 고립을 담당하는 영역은 <strong>dACC(전방대상피질)</strong>와 <strong>전방 뇌섬엽(Anterior Insula)</strong>입니다. 놀랍게도 이 영역은 우리가 불에 데이거나 칼에 베이었을 때, 즉 <strong>실제 신체적 고통</strong>을 인지하는 부위와 정확히 일치합니다.</p>

<p>Nature Neuroscience의 최신 연구에 따르면, 뇌는 고립을 '심리적 문제'가 아닌 '물리적 위협'으로 처리합니다. 당신이 느끼는 지독한 외로움은 당신의 뇌가 생존을 위해 보내는 가장 강렬한 <strong>통증 신호</strong>인 셈입니다.</p>

<h3>2. 고립이 뇌에 남기는 흉터</h3>
<p>고립이 만성화되면 전두엽(PFC)의 집행 기능이 급격히 저하됩니다. 이 상태의 뇌는 주권을 잃고, 타인에게 의존하거나 '거짓된 각본(사기)'에 중독되기 가장 쉬운 취약한 상태가 됩니다.</p>

<p><strong>결론:</strong> 당신이 느끼는 외로움은 나약함의 증거가 아닙니다. 그것은 당신의 생존 본능이 "지금 당장 연결의 주권을 회복하라"고 외치는 과학적 신호입니다.</p>

<hr />

<p><em>본 콘텐츠는 [2-Step 연쇄 발행] 중 1단계 '과학적 분석'입니다. 곧 이어질 2단계 '철학적 통찰'에서는 이 신경학적 고통을 인간이 어떻게 '자기기만'이라는 감옥으로 치환하는지, 그 실존적 해법을 다룹니다.</em></p>

<p><strong>[데이터 출처]</strong><br />
Nature Neuroscience: <a href="https://www.nature.com/neuro">https://www.nature.com/neuro</a><br />
Cognitive Brain Research: <a href="https://www.sciencedirect.com/journal/cognitive-brain-research">Journal Archive</a></p>
"""

publish_post(title, content, status='publish')
