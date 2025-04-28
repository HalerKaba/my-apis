from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Fake tweets database
tweets = []

# Fake notifications database
notifications = [
    "User123 liked your tweet!",
    "New follower: FlutterDev",
    "Your post reached 100 likes!",
    "Welcome to the app!"
]

class Tweet(BaseModel):
    user: str
    content: str

@app.get("/")
def read_root():
    return {"message": "Welcome to My Twitter Clone API!"}

@app.get("/tweets")
def get_tweets():
    return tweets

@app.post("/tweets")
def post_tweet(tweet: Tweet):
    tweets.append(tweet.dict())
    return {"message": "Tweet posted successfully"}

@app.get("/notifications")
def get_notifications():
    return notifications
