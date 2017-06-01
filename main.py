from amazon.api import AmazonAPI

from config import AWSACCESSKEY, AWSSECRETKEY, AMAZONSTORE

class AmazonBooker:
    def __init__(self):
        self.amazon = AmazonAPI(AWSACCESSKEY, AWSSECRETKEY, AMAZONSTORE)

    def get_book_by_name(self, name):
        return self.amazon.search_n(1, Keywords=name, SearchIndex='Books')[0]

    def get_books_by_name(self, name, num):
        return self.amazon.search_n(num, Keywords=name, SearchIndex='Books')


if __name__ == "__main__":
    amazonBooker = AmazonBooker()
