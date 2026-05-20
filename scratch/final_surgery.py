from scripts.web_master_surgery import perform_surgery
import os

data = {
    'id': 'isolation-brain-pain',
    'title': '고립된 뇌가 느끼는 통증의 실체',
    'excerpt': '“고요함이 통증으로 번지는 순간, 뇌는 연결이라는 생존의 빛을 갈구한다.” - 사회적 고립이 뇌에 미치는 파괴적 영향과 진화론적 통찰.',
    'categories': ['Science', 'Neuroscience'],
    'image': 'https://insights.sociallogiclab.org/wp-content/uploads/2026/05/isolated_brain_pain_rembrandt_v1_1778822314569.jpg',
    'content': '<h3>과학적 통찰: 뇌는 고립을 부상으로 인식한다</h3><p>UCLA의 연구에 따르면, 사회적 고립 시 뇌의 dACC 부위가 활성화되며 이는 신체적 통증과 동일한 메커니즘입니다...</p>'
}

js_path = r'c:\AI\connect-ai\main_design\assets\index-5EKcGoY5.js'
perform_surgery(js_path, data)
print("[Web Master] Final surgery with caption completed successfully.")
