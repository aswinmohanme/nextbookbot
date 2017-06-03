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
    tweet_body = ["Hey @{} try {} on {} #books #suggest",
                 "Hey @{} Checkout {} on {} #books #suggest",
                 "Hey @{} This seems #interesting {} on {} #books #suggest #books",
                 "Hey @{} just found this {} on {} for #you #suggest #books",
                 "Hey @{} thinking about giving {} at {} a #try #suggest #books"
                 ]

    # Main Function CallBack
    def process_status(status):
        try:
            if status.lang == "en":
                keywords = Rake.run(status.text.replace('#', '').replace('@nextbookbot', ''))
                books = amazonBooker.get_similar_books(' '.join([x[0] for x in keywords[:4]]), 4)
                book = random.choice(books)

                # Tweet to the User who Tweeted it 
                status_txt = random.choice(tweet_body).format(status.user.screen_name, book.title[:30], book.offer_url)
                tweeter.update_status(status_txt, status.id)

                print(status_txt)
                with open('log.txt', 'a') as log:
                    log.write(status_txt)
                    log.write('\n')

        except amazon.api.SearchException:
            tweeter.update_status("Hey @{} I can't find that Book, it must be me ,can you try once more with the exact name of the book?".format(status.user.screen_name))


    tweeter.create_stream(process_status)
    tweeter.track_stream(['@nextbookbot', "#mynextread"])

