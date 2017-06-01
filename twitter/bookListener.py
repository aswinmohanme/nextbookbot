
import tweepy

# Implements a Stream Listener
class BookListener(tweepy.StreamListener):

    def status_callback(self, cb):
        self.cb = cb

    # Override CallBack to respond on status
    def on_status(self, status):
        self.cb(status)

    def on_error(self, status_code):
        if status_code == 420:
            return False