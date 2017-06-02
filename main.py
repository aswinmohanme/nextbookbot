
from amazonBooker import AmazonBooker
from twitter.tweeter import Tweeter


# Get Tweets with #book or #books and then Tweet with the Amazon Affiliate Link
if __name__ == "__main__":
    amazonBooker = AmazonBooker()
    tweeter = Tweeter()

    # Main Function CallBack
    def process_status(status):
        if status.lang == "en":
            with open('tweet.txt', 'a') as f:
                f.write(status.text + '\n')

    tweeter.create_stream(process_status)
    tweeter.track_stream(['books'])

