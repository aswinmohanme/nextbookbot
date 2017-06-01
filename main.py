
from amazonBooker import AmazonBooker
from twitter.tweeter import Tweeter

# Get Tweets with #book or #books and then Tweet with the Amazon Affiliate Link
if __name__ == "__main__":
    amazonBooker = AmazonBooker()
    tweeter = Tweeter()

    for tweet in tweeter.get_tweets_from_hashtag("#books"):
        print(tweet.user.screen_name)

