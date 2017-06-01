
from amazonBooker import AmazonBooker
from twitter.tweeter import Tweeter

# Get Tweets with #book or #books and then Tweet with the Amazon Affiliate Link
if __name__ == "__main__":
    amazonBooker = AmazonBooker()
    tweeter = Tweeter()

    tweeter.create_stream()
    tweeter.track_stream('books')

