# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tweet(BaseModel):
    id: int
    user: str
    content: str
    likes: int = 0

# Fake Database
tweets: List[Tweet] = []

@app.get("/tweets", response_model=List[Tweet])
def get_tweets():
    return tweets

@app.post("/tweets", response_model=Tweet)
def create_tweet(tweet: Tweet):
    tweets.append(tweet)
    return tweet

@app.post("/tweets/{tweet_id}/like", response_model=Tweet)
def like_tweet(tweet_id: int):
    for tweet in tweets:
        if tweet.id == tweet_id:
            tweet.likes += 1
            return tweet
    return {"error": "Tweet not found"}
