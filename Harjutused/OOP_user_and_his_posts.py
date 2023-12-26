"""
Loo klassid Post ja User. Kasutajal on meetodid create_post(), mis lisab postitused kasutajale ja like_post(),
ning postitusel def like(). Postitusel peab olema likes, mis näitab, mitu meeldimist sellel on ning kasutajal on posts,
mis hoiab kõiki tema postitusi.
"""


class Post:
    def __init__(self, content, author_name):
        self.content = content
        self.author_name = author_name
        self.likes = 0

    def like(self):
        self.likes += 1


class User:
    def __init__(self, username):
        self.username = username
        self.posts = []


    def create_post(self, content):
        new_post = Post(content, self.username)
        self.posts.append(new_post)
        return new_post

    def like_post(self, post):
        post.like()



user1 = User("Alice")
user2 = User("Bob")

post1 = user1.create_post("Hello, this is my first post!")
print(f"{post1.author_name} posted: {post1.content}")

post2 = user2.create_post("Nice weather today!")
print(f"{post2.author_name} posted: {post2.content}")

user1.like_post(post2)
print(f"{user1.username} liked {post2.author_name}'s post.")

for post in user1.posts:
    print(f"{post.content} | Likes: {post.likes}")