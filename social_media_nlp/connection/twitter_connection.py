import tweepy
from script.load_config import load_config

class TwitterConnection:
    def __init__(self):
        config = load_config()
        twitter_secrets = config.get("twitter", {})

        self.api_key = twitter_secrets.get("api_key")
        self.api_secret = twitter_secrets.get("api_secret")
        self.access_token = twitter_secrets.get("access_token")
        self.access_secret = twitter_secrets.get("access_secret")

        self.client = self._authenticate()

    def _authenticate(self):
        """Autentica na API do Twitter e retorna um cliente do Tweepy"""
        try:
            auth = tweepy.OAuth1UserHandler(
                self.api_key, self.api_secret,
                self.access_token, self.access_secret
            )
            return tweepy.API(auth, wait_on_rate_limit=True)
        except Exception as e:
            raise ConnectionError(f"Erro ao conectar na API do Twitter: {e}")

    def get_client(self):
        """Retorna o cliente autenticado do Tweepy"""
        return self.client
