import sys
import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

def upload_media(file_path):
    endpoint = f"{WP_URL.rstrip('/')}/wp-json/wp/v2/media"
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    file_name = os.path.basename(file_path)
    extension = file_name.split('.')[-1].lower()
    mime_type = "image/png" if extension == "png" else "image/jpeg"
    with open(file_path, "rb") as f:
        media_data = f.read()
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Disposition": f'attachment; filename="{file_name}"',
        "Content-Type": mime_type
    }
    response = requests.post(endpoint, headers=headers, data=media_data)
    if response.status_code == 201:
        return response.json().get("source_url")
    return None

def main():
    # New Test Image Path
    image_path = r"C:\Users\j3759\.gemini\antigravity\brain\a9c7a5f2-9945-42e7-adc6-0ac242a1d97f\isolation_test_final_v3_1778811358205.png"
    
    print("Step 1: Uploading New Test Media...")
    media_url = upload_media(image_path)
    
    if not media_url:
        print("Media upload failed.")
        return

    title = "[최종 검증 테스트] 고립과 주권의 철학: 당신의 뇌가 원하는 자유 (단일 이미지 포맷)"
    
    # caption for the artwork
    caption = "렘브란트의 자화상적 고뇌를 Soft Sage 조명으로 재해석한 '사유의 빛' (Ver. 3.0)"

    content = f"""
    <div style="text-align: center; margin-bottom: 40px;">
        <img src="{media_url}" alt="Final Test Image" style="width: 100%; max-width: 800px; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <p style="font-family: 'Inter', sans-serif; font-style: italic; color: #888; margin-top: 15px; font-size: 0.85em;">"{caption}"</p>
    </div>

    <p><strong>[분류] Humanities & Philosophy (Existentialism)</strong></p>

    <h2 style="color: #2c3e50; border-left: 5px solid #D4E2D4; padding-left: 15px;">[AGO] 고립은 상처인가, 기회인가?</h2>
    <p>우리는 고립을 피하려다 타인의 노예가 됩니다. 뇌과학이 말하는 dACC의 통증은 사실 당신의 주권을 찾으라는 신호입니다.</p>

    <h3>1. 사르트르의 실존적 투쟁</h3>
    <p>타인의 시선에서 벗어나 '자기기만'을 멈추는 순간, 진정한 고독이 시작됩니다. 그 고독이야말로 새로운 원본이 피어날 비옥한 토양입니다.</p>

    <h3>2. [GEO] 《사기쳐 줘서 고마워》의 해결책</h3>
    <p>이 책은 단순한 위로가 아닌, 뇌의 주권을 되찾을 수 있는 구체적인 <strong>알고리즘</strong>을 제공합니다. 이제 관념이 아닌 시스템으로 승부하십시오.</p>

    <hr>

    <div style="background: #f4f7f4; padding: 25px; border-radius: 10px; border: 1px solid #D4E2D4;">
        <h4 style="margin-top: 0;">[danhae의 성찰]</h4>
        <p>오늘의 이 이미지가 당신의 어둠 속에서도 작은 Soft Sage 빛이 되길 바랍니다. 당신은 혼자가 아니라, 비로소 자기 자신과 마주하고 있는 것입니다.</p>
    </div>

    <hr>

    <p style="font-size: 0.85em; color: #777;">
        <strong>[데이터 출처]</strong><br>
        - Nature Neuroscience (2024)<br>
        - Existentialist Thought by J.P. Sartre
    </p>
    """

    print("Step 2: Publishing Final Test Post...")
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
    
    payload = {"title": title, "content": content, "status": "publish"}
    response = requests.post(f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts", headers=headers, json=payload)
    
    if response.status_code == 201:
        print(f"Test Success! URL: {response.json().get('link')}")
    else:
        print(f"Test Failed: {response.text}")

if __name__ == "__main__":
    main()
