
from amazonBooker import AmazonBooker
from twitter.tweeter import Tweeter

def print_status(status):
    print(status.text)

# Get Tweets with #book or #books and then Tweet with the Amazon Affiliate Link
if __name__ == "__main__":
    amazonBooker = AmazonBooker()
    tweeter = Tweeter()

    tweeter.create_stream(print_status)
    tweeter.track_stream('books')

