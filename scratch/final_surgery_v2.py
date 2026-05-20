import os
import re
import json
import shutil
from datetime import datetime

def perform_surgery(js_path, new_post_data):
    backup_path = js_path + ".bak"
    try:
        shutil.copy2(js_path, backup_path)
    except:
        pass

    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(Rh=\[)'
    post_id = new_post_data.get('id', 'new-insight-' + datetime.now().strftime('%m%d'))
    title = new_post_data.get('title', 'Untitled Insight')
    excerpt = new_post_data.get('excerpt', '')
    categories = new_post_data.get('categories', ["Philosophy"])
    date_str = datetime.now().strftime('%b %d, %Y')
    image_url = new_post_data.get('image', '')
    body_content = new_post_data.get('content', '').replace('`', '\\`').replace('${', '\\${')

    new_post_js = f'{{id:"{post_id}",title:"{title}",excerpt:"{excerpt}",category:"Latest Insight",categories:{json.dumps(categories, ensure_ascii=False)},date:"{date_str}",readTime:"5 min read",image:"{image_url}",featured:!0,isMemberOnly:!1,content:`{body_content}`}},'

    if re.search(pattern, content):
        updated_content = re.sub(pattern, r'\1' + new_post_js, content)
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    return False

data = {
    'id': 'isolation-brain-pain',
    'title': '고립된 뇌가 느끼는 통증의 실체',
    'excerpt': '“고요함이 통증으로 번지는 순간, 뇌는 연결이라는 생존의 빛을 갈구한다.” - 사회적 고립이 뇌에 미치는 파괴적 영향과 진화론적 통찰.',
    'categories': ['Science', 'Neuroscience'],
    'image': 'https://insights.sociallogiclab.org/wp-content/uploads/2026/05/isolated_brain_pain_rembrandt_v1_1778822314569.jpg',
    'content': '<h3>과학적 통찰: 뇌는 고립을 부상으로 인식한다</h3><p>UCLA의 연구에 따르면, 사회적 고립 시 뇌의 dACC 부위가 활성화되며 이는 신체적 통증과 동일한 메커니즘입니다...</p>'
}

js_path = r'c:\AI\connect-ai\main_design\assets\index-5EKcGoY5.js'
if perform_surgery(js_path, data):
    print("[Web Master] Final surgery with caption completed successfully.")
else:
    print("[Web Master] Surgery failed.")
