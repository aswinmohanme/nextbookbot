
import tweepy

from . import twitterConfig
from . import bookListener

class Tweeter:
    def __init__(self):
        self.auth = self._authenticate()
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        self.bookStream = None
    
    # Authenticate the Twitter Client
    def _authenticate(self):
        TCONSUMERKEY, TCONSUMERSECRET = twitterConfig.TCONSUMERKEY, twitterConfig.TCONSUMERSECRET
        TACCESSTOKEN, TACCESSTOKENSECRET = twitterConfig.TACCESSTOKEN, twitterConfig.TACCESSTOKENSECRET

        auth = tweepy.OAuthHandler(TCONSUMERKEY, TCONSUMERSECRET)
        auth.set_access_token(TACCESSTOKEN, TACCESSTOKENSECRET)

        return auth

    # Send A Tweet
    def update_status(self, status, reply_id):
        if len(status) > 140:
            print("The Length of Status Must be less than 140")
            return None

        self.api.update_status(status, in_reply_to_status_id=reply_id)
    
    # Return a List of Tweets for a given hash tag
    def get_tweets_from_hashtag(self, hashtag, limit=None):
        return tweepy.Cursor(self.api.search, q=hashtag).items()

    # Create and Return a Stream
    def create_stream(self, cb):
        bookStreamListener = bookListener.BookListener()
        bookStreamListener.status_callback(cb)
        self.bookStream = tweepy.Stream(auth=self.api.auth, listener=bookStreamListener)
    
    # Track which Hastag
    def track_stream(self, tag):
        self.bookStream.filter(track=tag)
       
