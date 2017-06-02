import time
import random

import RAKE
import amazon

from amazonBooker import AmazonBooker
from twitter.tweeter import Tweeter

# Get Tweets with #book or #books and then Tweet with the Amazon Affiliate Link
if __name__ == "__main__":
    amazonBooker = AmazonBooker()
    tweeter = Tweeter()
    Rake = RAKE.Rake('smartStop.txt')

    tweet_body = ["Hey there @{} I just found this book {} that you would love to read",
                  "Hey @{} since you like reading so much, Check out {}",
                  "@{} I just read your last tweet and thought you would love {}"]

    # Main Function CallBack
    def process_status(status):
        try:
            if status.lang == "en":
                keywords = Rake.run(status.text.replace('#', ''))
                book = amazonBooker.get_book_by_keywords(' or '.join([x[0] for x in keywords[:3]]))

                time.sleep(5)
                # Tweet to the User who Tweeted it 
                tweeter.update_status(random.choice(tweet_body).format(status.user.screen_name, book.offer_url))
        except amazon.api.SearchException:
            pass

    tweeter.create_stream(process_status)
    tweeter.track_stream(['books'])

