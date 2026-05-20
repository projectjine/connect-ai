import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

WP_URL = os.getenv('WP_URL')
WP_USERNAME = os.getenv('WP_USERNAME')
WP_APP_PASSWORD = os.getenv('WP_APP_PASSWORD')

def update_post_slug(post_id, new_slug):
    endpoint = f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts/{post_id}"
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "slug": new_slug
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("link")
    return None

if __name__ == "__main__":
    # Latest post ID was 21
    new_link = update_post_slug(21, "scientific-analysis-isolation")
    if new_link:
        print(f"Update Success! New Link: {new_link}")
    else:
        print("Update Failed.")
