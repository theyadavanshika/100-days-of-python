from flask import Flask, render_template
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

blog_url = os.getenv("BLOG_URL")
response = requests.get(blog_url) 
all_posts = response.json() 

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html") 

@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None 

    for post in all_posts:
        if post["id"] == post_id:
            requested_post = post 

    return render_template("post.html", post=requested_post) 

if __name__ == "__main__":
    app.run(port=5001, debug=True)