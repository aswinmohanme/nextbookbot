
import tweepy

# Implements a Stream Listener
class BookListener(tweepy.StreamListener):
    
    # Override CallBack to respond on status
    def on_status(self, status):
        print(status.text)
