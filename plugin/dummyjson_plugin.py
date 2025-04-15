import requests
from config import BASE_URL
from plugin.base_plugin import BasePlugin

#plugin implementation for the DummyJSON API
class DummyJSONPlugin(BasePlugin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None

    #connectivity test - attempts login with provided credentials
    def login(self):
        try:
            response = requests.post(f"{BASE_URL}/auth/login", json={
                "username": self.username,
                "password": self.password
            })
            response.raise_for_status()
            self.token = response.json().get("token")
            print("Login successful")
            return True
        except requests.RequestException as e:
            print(f"Login failed: {e}")
            return False

    #internal helper for authenticated headers
    def _auth_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    #E1 - Fetch user details after successful login
    def collect_user_details(self):
        try:
            response = requests.get(f"{BASE_URL}/auth/me", headers=self._auth_headers())
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error collecting user details: {e}")
            return {}

    #E2 - Collect a list of 60 posts
    def collect_posts(self):
        try:
            response = requests.get(f"{BASE_URL}/posts?limit=60")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error collecting posts: {e}")
            return {}

    #E3 - Collect the same posts with their comments
    def collect_posts_with_comments(self):
        posts_data = self.collect_posts()
        posts = posts_data.get("posts", [])
        for post in posts:
            try:
                comments_resp = requests.get(f"{BASE_URL}/posts/{post['id']}/comments")
                comments_resp.raise_for_status()
                post["comments"] = comments_resp.json().get("comments", [])
            except requests.RequestException as e:
                print(f"Failed to get comments for post {post['id']}: {e}")
                post["comments"] = []
        return posts
