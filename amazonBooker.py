from amazon.api import AmazonAPI
import random

from config import AWSACCESSKEY, AWSSECRETKEY, AMAZONSTORE

class AmazonBooker:
    def __init__(self):
        self.amazon = AmazonAPI(AWSACCESSKEY, AWSSECRETKEY, AMAZONSTORE)

    def get_book_by_name(self, name):
        return self.amazon.search_n(1, Keywords=name, SearchIndex='Books')[0]

    def get_books_by_name(self, name, num):
        return self.amazon.search_n(num, Keywords=name, SearchIndex='Books')

    def get_book_by_keywords(self, kw):
        return self.amazon.search_n(1, Power=kw, SearchIndex='Books')[0]
    
    def get_similar_books(self, name, num):
        # book = self.amazon.search_n(1, Power='title:({})'.format(name), SearchIndex='Books')[0]
        book = self.amazon.search_n(1, Keywords=name, SearchIndex='Books')[0]
        books = self.amazon.similarity_lookup(ItemId=book.asin)
        return books[:num]
    