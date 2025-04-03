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
        tweets = self.client.search_recent_tweets(query=query, max_results=max_tweets)
        return tweets.data if tweets.data else []

