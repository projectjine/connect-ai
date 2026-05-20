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
    media_id = 10
    media_url = "https://insights.sociallogiclab.org/wp-content/uploads/2026/05/isolation_philosophical_rembrandt_1778810888844-1.jpg"
    
    title = "[V3 엔진 테스트] 당신의 외로움이 물리적 '통증'인 이유"

    # Gutenberg Block-based Content matching the "Detail Engine"
    content = f"""
<!-- wp:paragraph {{"align":"center","className":"insight-category"}} -->
<p class="has-text-align-center insight-category" style="color:#4a654e;font-size:13px;font-weight:700;letter-spacing:2px;">NEUROSCIENCE &amp; PHILOSOPHY</p>
<!-- /wp:paragraph -->

<!-- wp:image {{"id":{media_id},"sizeSlug":"large","linkDestination":"none","className":"is-style-default"}} -->
<figure class="wp-block-image size-large is-style-default"><img src="{media_url}" alt="고립된 뇌의 신경망" class="wp-image-{media_id}"/><figcaption class="wp-element-caption">고립의 순간 dACC(전방대상피질)에서 발생하는 전기적 신호를 시각화한 형상.</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>우리의 뇌는 혼자 남겨지는 것을 물리적 상처만큼이나 고통스럽게 인식합니다. 최근 신경과학 연구에 따르면, 사회적 고립 시 활성화되는 뇌의 영역은 뼈가 부러질 때 반응하는 통증 네트워크와 정확히 일치합니다.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":2}} -->
<h2 class="wp-block-heading">[AGO] 연결되지 않은 자아의 비명</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>디지털이 모든 것을 연결하는 시대라지만, 역설적으로 우리는 가장 고립되어 있습니다. 스크린 너머의 무수한 '좋아요'는 도파민을 단기적으로 분비시킬 뿐, 옥시토신을 생성하는 진정한 연결(Deep Connection)을 대체하지 못합니다. 뇌는 이 가짜 연결을 알아채고 계속해서 결핍의 경고음을 울립니다.</p>
<!-- /wp:paragraph -->

<!-- wp:quote {{"className":"is-style-default"}} -->
<blockquote class="wp-block-quote is-style-default"><p>"혼자임을 선택한 고독(Solitude)은 우리를 단단하게 만들지만, 강요된 고립(Isolation)은 우리의 신경망을 파괴한다. 진정한 연결은 스크린을 끄고 상대방의 눈동자에 나의 시선을 온전히 머물게 할 때 비로소 시작된다."</p><cite>Danhae's Reflection</cite></blockquote>
<!-- /wp:quote -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">[CEO] 고립을 권력으로 바꾸는 '원본 회복 알고리즘'</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>고립은 결코 나약함의 증거가 아닙니다. 오히려 '가짜 나'를 거부하는 영혼의 강력한 저항입니다. 뇌과학이 증명하듯, 고립의 통증은 당신의 주권 회복을 위한 '성장통'에 불과합니다. 이제 그 통증을 온전히 받아들이고, 당신만의 독창적 사유(Originality)를 위한 자양분으로 삼으십시오. 무의미한 소음을 차단하고 당신의 내면으로 하강할 때, 고립은 곧 가장 묵직한 무기가 됩니다.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"center"}}}} -->
<div class="wp-block-buttons"><!-- wp:button {{"className":"is-style-outline"}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="https://sociallogiclab.org">더 깊은 통찰력 알아보기</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">관련된 다른 통찰 읽기</h3>
<!-- /wp:heading -->

<!-- wp:latest-posts {{"displayPostDate":true,"displayFeaturedImage":false,"columns":2,"displayPostContent":false,"className":"is-style-default"}} /-->
"""

    print("Step 1: Publishing Post with Detail Engine Blocks...")
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
    
    payload = {
        "title": title, 
        "content": content, 
        "status": "publish",
        "featured_media": media_id  # Keeps thumbnail logic intact, while CSS hides the auto top image
    }
    
    response = requests.post(f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts", headers=headers, json=payload)
    
    if response.status_code == 201:
        post_id = response.json().get("id")
        print(f"Success! Post ID: {post_id}")
        print(f"URL: {response.json().get('link')}")
    else:
        print(f"Failed to publish: {response.text}")

if __name__ == "__main__":
    main()
