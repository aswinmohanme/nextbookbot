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
    users_tweeted = ["abookme"]
    # tweet_body = ["Hey there @{} I just found this book {} that you would love to read #books #read",
    #               "Hey @{} since you like reading so much, Check out {} #toread #read #books",
    #               "@{} I just read your last tweet and thought you would love {} #toread #books",
    #               "Hey @{} Thought you would #love {} #books #fead",
    #               "Hey @{} Check out this awesome book that you will love {} #books",
    #               "Hey @{} I am thinking you would #love {} #books"]
    tweet_body = ["Hey @{} I just found {} on {} that you would love #books ",
                  "Hey @{} since you like reading, Check {} on {} #books",
                  "@{} I think you will love {} on {} #toread #books",
                  "Hey @{} I bet you will fall in #love with {} on {} #books ",
                  "Hey @{} Check out this awesome book  {} on {} #books",
                  "Hey @{} I am thinking you would #love {} on {} #books"]

    # Main Function CallBack
    def process_status(status):
        try:
            if status.lang == "en" and status.user.screen_name not in users_tweeted: 
                keywords = Rake.run(status.text.replace('#', ''))
                book = amazonBooker.get_book_by_keywords(' or '.join([x[0] for x in keywords[:4]]))

                time.sleep(random.randrange(60,120))
                # Tweet to the User who Tweeted it 
                status_txt = random.choice(tweet_body).format(status.user.screen_name, book.title[:20], book.offer_url)

                users_tweeted.append(status.user.screen_name)
                tweeter.update_status(status_txt, status.id)

                print(status_txt)
                with open('log.txt', 'a') as log:
                    log.write(status_txt)
                    log.write('\n')

        except amazon.api.SearchException:
            pass


    tweeter.create_stream(process_status)
    tweeter.track_stream(['books', '#books'])

