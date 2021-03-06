from datetime import datetime
import instaloader

L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, "instagram")
posts = profile.get_posts()

for post in posts.between(start=datetime(2020, 11, 27), end=datetime(2020, 11, 30)):
    L.download_post(post, "instagram")
