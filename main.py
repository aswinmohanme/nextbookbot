
from amazonBooker import AmazonBooker
from twitter.tweeter import Tweeter

if __name__ == "__main__":
    amazonBooker = AmazonBooker()
    tweeter = Tweeter()

    tweeter.update_status("Hey There Test")
