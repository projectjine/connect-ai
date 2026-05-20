import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

WP_URL = os.getenv('WP_URL')
WP_USERNAME = os.getenv('WP_USERNAME')
WP_APP_PASSWORD = os.getenv('WP_APP_PASSWORD')

def check_recent_posts():
    auth = base64.b64encode(f"{WP_USERNAME}:{WP_APP_PASSWORD}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=10", headers=headers)
    if r.status_code == 200:
        for p in r.json():
            print(f"ID: {p['id']}, Title: {p['title']['rendered']}, Status: {p['status']}, Link: {p['link']}")
    else:
        print(f"Error: {r.status_code}")

if __name__ == "__main__":
    check_recent_posts()
