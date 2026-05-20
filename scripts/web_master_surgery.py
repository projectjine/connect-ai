import os
import re
import json
import shutil
from datetime import datetime

def perform_surgery(js_path, new_post_data):
    """
    Performs 'precision surgery' on the minified JS file to inject a new post into the Rh array.
    Ensures UTF-8 encoding and validates image URLs to prevent X-box issues.
    """
    backup_path = js_path + ".bak"
    
    # 1. Backup safety
    try:
        shutil.copy2(js_path, backup_path)
        print(f"[Web Master] Backup created at {backup_path}")
    except Exception as e:
        print(f"[Web Master] Warning: Backup failed but continuing. {e}")

    # 2. Read the patient (JS file) with strict UTF-8
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3. Identify the Rh array pattern: Rh=[{...}]
    pattern = r'(Rh=\[)'
    
    # Data Preparation
    post_id = new_post_data.get('id', 'new-insight-' + datetime.now().strftime('%m%d'))
    title = new_post_data.get('title', 'Untitled Insight')
    excerpt = new_post_data.get('excerpt', '')
    categories = new_post_data.get('categories', ["Philosophy"])
    date_str = datetime.now().strftime('%b %d, %Y')
    
    # Image Path Optimization (Ensure absolute URL)
    image_url = new_post_data.get('image', '')
    if image_url and not image_url.startswith(('http://', 'https://')):
        # Default domain if relative path provided
        BASE_URL = "https://yourdomain.com" # Should be updated to actual domain
        image_url = f"{BASE_URL}/{image_url.lstrip('/')}"

    # Escape for JS template literals
    body_content = new_post_data.get('content', '').replace('`', '\\`').replace('${', '\\${')

    # Construct the new JS object string (Minified style)
    new_post_js = f'{{id:"{post_id}",title:"{title}",excerpt:"{excerpt}",category:"Latest Insight",categories:{json.dumps(categories, ensure_ascii=False)},date:"{date_str}",readTime:"5 min read",image:"{image_url}",featured:!0,isMemberOnly:!1,content:`{body_content}`}},'

    if re.search(pattern, content):
        # Inject as the first item in the array
        updated_content = re.sub(pattern, r'\1' + new_post_js, content)
        
        # 4. Save the patient with strict UTF-8
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"[Web Master] Surgery successful. Post '{title}' injected with UTF-8 integrity.")
        return True
    else:
        print("[Web Master] Error: Rh array not found. The JS structure might have changed.")
        return False

if __name__ == "__main__":
    # Test sample
    TEST_JS = r"c:\AI\connect-ai\main_design\assets\index-5EKcGoY5.js"
    sample_data = {
        "id": "isolation-science-v3",
        "title": "[V3 엔진 테스트] 당신의 외로움이 물리적 '통증'인 이유",
        "excerpt": "고립될 때 뇌에서 활성화되는 영역은 뼈가 부러질 때 반응하는 통증 네트워크와 일치합니다. V3 무결점 엔진이 텍스트만으로 만들어낸 완벽한 레이아웃을 확인하세요.",
        "categories": ["Neuroscience", "V3 Engine"],
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=1200",
        "content": "<p>워드프레스에서 V3 자동화 디자인을 확인하세요.</p><a href='https://insights.sociallogiclab.org/v3-%ec%97%94%ec%a7%84-%ed%85%8c%ec%8a%a4%ed%8a%b8-%eb%8b%b9%ec%8b%a0%ec%9d%98-%ec%99%b8%eb%a1%9c%ec%9b%80%ec%9d%b4-%eb%ac%bc%eb%a6%ac%ec%a0%81-%ed%86%b5%ec%a6%9d%ec%9d%b8-%ec%9d%b4%ec%9c%a0/' class='wp-block-button__link'>전체 글 읽기</a>"
    }
    perform_surgery(TEST_JS, sample_data)
