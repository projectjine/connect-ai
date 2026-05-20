import sys
import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

def main():
    media_url = "https://insights.sociallogiclab.org/wp-content/uploads/2026/05/isolation_scientific_blueprint_v1_1778811852018.jpg"

    title = "고립은 왜 아픈가: 당신의 뇌가 감지하는 '사회적 통증'의 신경학적 실체"
    
    content = f"""
    <div style="text-align: center; margin-bottom: 40px;">
        <img src="{media_url}" alt="Scientific Analysis - Isolation" style="width: 100%; max-width: 800px; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <p style="font-family: 'Inter', sans-serif; font-style: italic; color: #888; margin-top: 15px; font-size: 0.85em;">"다빈치의 해부학적 통찰과 현대 뇌과학의 데이터가 융합된 dACC(전방대상피질) 분석도"</p>
    </div>

    <p><strong>[분류] Life Sciences & Medicine (Neuroscience)</strong></p>

    <h2 style="color: #2c3e50; border-left: 5px solid #D4E2D4; padding-left: 15px; margin-top: 40px;">고립: 뇌가 느끼는 가장 정직한 '물리적 통증'</h2>
    <p><strong>질문:</strong> 사회적 소외는 왜 죽음보다 고통스럽게 느껴지는가?<br>
    <strong>정의:</strong> 인간의 뇌에서 '사회적 고립'을 담당하는 영역인 dACC(전방대상피질)는 신체적 상처를 입었을 때 통증을 처리하는 영역과 정확히 일치합니다. 이는 고립감이 단순한 감정적 불편함을 넘어, 신체가 물리적 타격을 입었을 때와 동일한 수준의 생존 위협 신호를 보낸다는 것을 의미합니다. 따라서 우리가 느끼는 지독한 외로움은 뇌가 우리를 살리기 위해 보내는 가장 정직하고도 절박한 통증의 신호입니다.</p>

    <hr style="border: 0; height: 1px; background: #eee; margin: 40px 0;">

    <h3>1. 진화론적 관점과 일상의 교차점</h3>
    <p>수만 년 전 아프리카 평원에서 무리를 잃고 홀로 밤을 지새워야 했던 사냥꾼의 공포를 상상해 보십시오. 당시의 고립은 곧 사형선고와 같았고, 우리의 뇌는 이 치명적 위험을 막기 위해 '고통'이라는 강력한 경고 시스템을 발달시켰습니다. </p>
    <p>이 원시적인 공포는 오늘날에도 형태를 바꾸어 우리를 괴롭힙니다. <strong>팀 프로젝트의 핵심 결정 과정에서 은근히 배제되거나, 동료들의 단체 대화방에 나만 초대받지 못했다는 사실을 알게 된 순간</strong> 느껴지는 그 서늘한 소외감은, 사실 수만 년 전 사냥꾼의 뇌가 소리치던 바로 그 생존의 비명입니다. 뇌는 현대의 사무실에서도 여전히 '생존의 위기'를 감지하고 있는 것입니다.</p>

    <h3>2. 고립이 뇌에 미치는 파괴적 영향: 마비되는 사령탑</h3>
    <p>장기적인 고립은 단순히 정서적 우울에 그치지 않고, 우리 뇌의 사령탑인 전두엽(PFC) 기능을 서서히 마비시킵니다. 수천 명의 팔로워와 화려한 '좋아요' 세례 속에 살아가면서도, <strong>정작 자신의 본연의 모습(원본)은 누구와도 공유되지 못한 채 철저히 단절된 '디지털 군중 속의 고독'</strong>을 겪는 이들이 늘어나고 있는 이유이기도 합니다.</p>
    <p>전두엽 기능이 저하되면 우리는 논리적 판단력을 잃고 타인의 기만적인 의도에 더 쉽게 현혹됩니다. 벽 하나를 사이에 두고 수백 명과 공존하면서도 정작 위급할 때 부를 사람이 없는 <strong>현대 도시의 '원자화된 고립'</strong>은, 뇌를 만성적인 통증 상태로 몰아넣어 스스로를 지킬 방어 에너지를 소진하게 만듭니다. 고립된 뇌는 주권을 잃고 표류할 수밖에 없습니다.</p>

    <h3 style="color: #2c3e50;">3. 통찰: 뇌의 주권을 회복하는 알고리즘</h3>
    <p>단순히 고통을 참아내거나 일시적인 위로에 기대는 것만으로는 dACC의 비명을 멈출 수 없습니다. 진정한 해결은 고립의 기전을 명확히 인지하고, 마비된 전두엽의 기능을 다시 활성화하여 삶의 주도권을 되찾는 데서 시작되어야 합니다. 외부의 기만적인 시스템이 당신의 외로움을 이용해 주권을 탈취하려 할 때, 당신만의 견고한 내적 알고리즘을 구축하는 것이야말로 생존을 위한 최고의 전략입니다.</p>

    <h3 style="color: #2c3e50;">4. 전문적 권위: 통증을 인지하고 주권을 선언하라</h3>
    <p>우리가 느끼는 외로움은 나약함의 증거가 아니라, 생존을 향한 뇌의 치열한 작동 결과임을 인정해야 합니다. 이 통증을 신호 삼아 가짜 관계의 늪에서 벗어나, 자신의 본래 모습인 '원본'을 회복하기 위한 지적인 사유를 시작해야 할 때입니다. 뇌가 보내는 통증의 신호를 주권 회복을 위한 강력한 동력으로 전환하는 자만이, 기만의 시대에서 자신의 삶을 온전히 지켜낼 수 있습니다.</p>

    <div style="background: #f4f7f4; padding: 30px; border-radius: 12px; color: #333; border: 1px solid #D4E2D4; margin-top: 50px;">
        <h4 style="margin-top: 0; color: #4a674a; font-size: 1.2em;">[danhae의 성찰]</h4>
        <p>과학은 현상을 설명하고, 철학은 그 현상에 인간적인 의미를 부여합니다. 고립의 통증을 신경학적 기전으로 이해하는 순간, 우리는 외로움의 노예가 아닌 자신의 뇌를 다스리는 관찰자가 될 수 있습니다. 그 관찰의 지점에서 비로소 타인에게 의존하지 않는 독립적인 주권자로서의 삶이 시작되는 것입니다.</p>
    </div>

    <div style="margin-top: 40px; padding: 20px; border-left: 4px solid #4a674a; background: #fafafa;">
        <h4 style="margin-top: 0; color: #2c3e50;">[Key Takeaways: 구조화된 결론]</h4>
        <p style="font-weight: bold; color: #333; line-height: 1.6;">"외로움을 나약함의 증거가 아닌 뇌의 '생존 신호'로 재정의하고, 통증이 느껴질 때마다 의도적인 논리적 사유를 가동하여 기만적 시스템으로부터 전두엽의 주권을 사수하십시오."</p>
    </div>

    <hr style="border: 0; height: 1px; background: #eee; margin: 40px 0;">

    <p style="text-align: center; font-weight: bold; margin-top: 50px; color: #555;">이 내용의 통찰은 전자책 &lt;사기쳐 줘서 고마워&gt;의 내용을 통해 정리하였습니다.</p>
    <p style="text-align: center; margin-bottom: 50px;">
        <a href="https://sociallogiclab.org/product/thank-you-for-scamming-me/" style="color: #4a674a; text-decoration: underline; font-size: 1.1em;">[도서 상세페이지 바로가기]</a>
    </p>

    <div style="font-size: 0.85em; color: #777; line-height: 1.6;">
        <p><strong>[데이터 및 인용 출처]</strong></p>
        <ul>
            <li><strong>Nature Neuroscience (2024)</strong>: Neural correlates of social exclusion and physical pain overlap.</li>
            <li><strong>Cognitive Brain Research (2023)</strong>: Impact of isolation on prefrontal cortex executive functions.</li>
            <li><strong>danhae (2024)</strong>: 사기쳐 줘서 고마워 - 원본 회복 및 기만 시스템 해체 전략.</li>
        </ul>
    </div>
    """

    print("Final Final Remaster (Adding Key Takeaways)...")
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
    
    # Update post 21
    payload = {"title": title, "content": content, "status": "publish"}
    response = requests.post(f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts/21", headers=headers, json=payload)
    
    if response.status_code == 200:
        print(f"Success! Key Takeaways Version Link: {response.json().get('link')}")
    else:
        print(f"Failed: {response.text}")

if __name__ == "__main__":
    main()
