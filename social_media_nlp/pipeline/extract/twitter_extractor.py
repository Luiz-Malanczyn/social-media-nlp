import json
import os
import tweepy
from script.load_config import load_config
from extract.base_extractor import BaseExtractor

class TwitterExtractor(BaseExtractor):
    def __init__(self):
        config = load_config()
        self.api_key = config["twitter"]["api_key"]
        self.api_secret = config["twitter"]["api_secret"]
        self.access_token = config["twitter"]["access_token"]
        self.access_secret = config["twitter"]["access_secret"]
        
        self.client = tweepy.Client(
            bearer_token=self.api_key,
            consumer_key=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_secret
        )

    def extract(self, query, max_tweets=100):
        tweets = self.client.search_recent_tweets(query=query, max_results=max_tweets, tweet_fields=["created_at", "author_id", "text"])
        tweets_data = tweets.data if tweets.data else []
        return [{"id": t.id, "author_id": t.author_id, "created_at": t.created_at, "text": t.text} for t in tweets_data]

    def save_to_json(self, data, filename="tweets_bronze.json"):
        os.makedirs("data/bronze", exist_ok=True)
        filepath = os.path.join("data/bronze", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Dados salvos em {filepath}")
