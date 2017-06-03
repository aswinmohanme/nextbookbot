from amazon.api import AmazonAPI
import random

from config import AWSACCESSKEY, AWSSECRETKEY, AMAZONSTORE

class AmazonBooker:
    def __init__(self):
        self.amazon = AmazonAPI(AWSACCESSKEY, AWSSECRETKEY, AMAZONSTORE)

    def get_book_by_name(self, name):
        return random.choice(self.amazon.search_n(3, Keywords=name, SearchIndex='Books'))

    def get_books_by_name(self, name, num):
        return self.amazon.search_n(num, Keywords=name, SearchIndex='Books')

    def get_book_by_keywords(self, kw):
        return self.amazon.search_n(1, Power=kw, SearchIndex='Books')[0]
    