import os
import requests
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

def upload_media(file_path):
    """
    Uploads an image to the WordPress Media Library with robust error handling.
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return None

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
    
    try:
        response = requests.post(endpoint, headers=headers, data=media_data)
        if response.status_code == 201:
            media_info = response.json()
            media_id = media_info.get("id")
            media_url = media_info.get("source_url")
            print(f"[OK] Media uploaded. ID: {media_id}, URL: {media_url}")
            return media_id, media_url
        else:
            print(f"[ERROR] Media upload failed: {response.status_code} - {response.text}")
            return None, None
    except Exception as e:
        print(f"[ERROR] Media upload exception: {str(e)}")
        return None, None

def publish_post(title, content, status='publish', featured_media=None):
    """
    Publishes a post. If featured_media is provided, it performs a two-step process:
    1. Create post without image (to avoid theme hook 500 errors).
    2. Update post with featured_media.
    """
    endpoint = f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts"
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
    
    # Step 1: Create the post
    payload = {
        "title": title,
        "content": content,
        "status": status
    }
    
    try:
        print(f"[INFO] Attempting to create post: {title}")
        response = requests.post(endpoint, headers=headers, json=payload)
        
        if response.status_code == 201:
            post_info = response.json()
            post_id = post_info.get("id")
            post_link = post_info.get("link")
            print(f"[OK] Post created successfully. ID: {post_id}")
            
            # Step 2: Attach featured media if provided
            if featured_media:
                print(f"[INFO] Attaching featured media (ID: {featured_media}) to post ID: {post_id}")
                update_endpoint = f"{endpoint}/{post_id}"
                update_payload = {"featured_media": featured_media}
                update_res = requests.post(update_endpoint, headers=headers, json=update_payload)
                
                if update_res.status_code == 200:
                    print(f"[OK] Featured media attached successfully.")
                else:
                    print(f"[WARNING] Failed to attach media: {update_res.status_code} - {update_res.text}")
            
            print(f"[SUCCESS] Final Post Link: {post_link}")
            return post_info
        else:
            print(f"[ERROR] {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"[ERROR] Exception: {str(e)}")
        return None

def delete_post(post_id):
    """
    Deletes a WordPress post by ID.
    """
    endpoint = f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts/{post_id}"
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}"}
    
    try:
        response = requests.delete(endpoint, headers=headers, params={"force": True})
        if response.status_code == 200:
            print(f"[OK] Post {post_id} deleted successfully.")
            return True
        else:
            print(f"[ERROR] Delete failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Exception: {str(e)}")
        return False

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="WordPress API Publisher & Media Uploader")
    parser.add_argument("--action", choices=["upload_media", "publish_post", "delete_post"], required=True)
    parser.add_argument("--file", help="Path to image file (required for upload_media)")
    parser.add_argument("--title", help="Post title")
    parser.add_argument("--content", help="Post content (HTML)")
    parser.add_argument("--status", default="publish", help="Post status (publish/draft)")
    parser.add_argument("--media_id", type=int, help="Featured media ID for the post")
    parser.add_argument("--post_id", type=int, help="Post ID for deletion")

    args = parser.parse_args()

    if args.action == "upload_media":
        if not args.file:
            print("[ERROR] --file is required for upload_media action.")
            sys.exit(1)
        upload_media(args.file)
    
    elif args.action == "publish_post":
        if not args.title or not args.content:
            print("[ERROR] --title and --content are required for publish_post action.")
            sys.exit(1)
        publish_post(args.title, args.content, args.status, args.media_id)

    elif args.action == "delete_post":
        if not args.post_id:
            print("[ERROR] --post_id is required for delete_post action.")
            sys.exit(1)
        delete_post(args.post_id)
