from social_media_nlp.pipeline.extract.twitter_extractor import TwitterExtractor


if __name__ == "__main__":
    extractor = TwitterExtractor()
    tweets = extractor.extract(query="OpenAI", max_tweets=1)
    extractor.save_to_json(tweets)
