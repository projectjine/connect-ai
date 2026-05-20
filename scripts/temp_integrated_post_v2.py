import sys
import os
import json
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
        return response.json().get("id"), response.json().get("source_url")
    return None, None

def main():
    image_path = r"C:\Users\j3759\.gemini\antigravity\brain\a9c7a5f2-9945-42e7-adc6-0ac242a1d97f\isolation_philosophical_rembrandt_1778810888844.png"
    title = "[철학적 통찰] 고립의 심연: 타인이라는 지옥에서 '나'의 주권을 회복하는 법"
    
    print("Step 1: Uploading Media...")
    media_id, media_url = upload_media(image_path)
    
    if not media_id:
        print("Media upload failed.")
        return

    content = f"""
    <div style="text-align: center; margin-bottom: 30px;">
        <img src="{media_url}" alt="Philosophical Insight" style="max-width: 100%; height: auto; border-radius: 8px;">
    </div>
    <h3>[분류] Humanities & Philosophy (Existentialism)</h3>
    <p>고립은 뇌가 보내는 생물학적 비명이자, 실존적 위기입니다...</p>
    <p>(중략)... 본문 내용 재구성 ...</p>
    <h4>[danhae의 성찰]</h4>
    <p>어둠 속에서 피어나는 Soft Sage 빛처럼, 고립의 고통을 뚫고 당신만의 고유한 빛을 찾으시길 바랍니다.</p>
    """

    # Step 1: Create Post WITHOUT featured image
    print("Step 2: Creating Post (Step 1/2)...")
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
    
    payload = {"title": title, "content": content, "status": "publish"}
    response = requests.post(f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts", headers=headers, json=payload)
    
    if response.status_code == 201:
        post_id = response.json().get("id")
        print(f"Post created. ID: {post_id}")
        
        # Step 2: Update Post WITH featured image
        print("Step 3: Attaching Featured Image (Step 2/2)...")
        update_payload = {"featured_media": media_id}
        update_response = requests.post(f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts/{post_id}", headers=headers, json=update_payload)
        
        if update_response.status_code == 200:
            print(f"Success! Link: {update_response.json().get('link')}")
        else:
            print(f"Failed to attach image: {update_response.text}")
    else:
        print(f"Post creation failed: {response.text}")

if __name__ == "__main__":
    main()
