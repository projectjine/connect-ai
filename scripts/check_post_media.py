import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

WP_URL = os.getenv('WP_URL')
WP_USERNAME = os.getenv('WP_USERNAME')
WP_APP_PASSWORD = os.getenv('WP_APP_PASSWORD')

def get_latest_post_and_media():
    auth = base64.b64encode(f"{WP_USERNAME}:{WP_APP_PASSWORD}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    
    # Get latest post
    r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=1", headers=headers)
    if r.status_code != 200:
        print(f"Error fetching posts: {r.status_code}")
        return
    
    post = r.json()[0]
    media_id = post.get("featured_media")
    print(f"Post Title: {post['title']['rendered']}")
    print(f"Featured Media ID: {media_id}")
    
    if media_id and media_id != 0:
        r_media = requests.get(f"{WP_URL}/wp-json/wp/v2/media/{media_id}", headers=headers)
        if r_media.status_code == 200:
            print(f"Media URL: {r_media.json().get('source_url')}")
        else:
            print(f"Error fetching media {media_id}: {r_media.status_code}")
    else:
        print("No featured media assigned.")

if __name__ == "__main__":
    get_latest_post_and_media()
