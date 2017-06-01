
import tweepy

from . import twitterConfig

class Tweeter:
    def __init__(self):
        self.auth = self._authenticate()
        self.api = tweepy.API(self.auth)

    def _authenticate(self):
        TCONSUMERKEY, TCONSUMERSECRET = twitterConfig.TCONSUMERKEY, twitterConfig.TCONSUMERSECRET
        TACCESSTOKEN, TACCESSTOKENSECRET = twitterConfig.TACCESSTOKEN, twitterConfig.TACCESSTOKENSECRET

        auth = tweepy.OAuthHandler(TCONSUMERKEY, TCONSUMERSECRET)
        auth.set_access_token(TACCESSTOKEN, TACCESSTOKENSECRET)

        return auth

    def update_status(self, status):
        if len(status) > 140:
            print("The Length of Status Must be less than 140")
            return None

        self.api.update_status(status)
