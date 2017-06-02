
import re

# Helper Class for easy tfidf score making
class TfIdf:
    def __init__(self):
        self.filename = "tweet.txt"
        self.lines = self._load_data()
    
    def _load_data(self):
        try:
           return self._clean_data(list(open(self.filename, 'r')))

        except IOError:
            print("File Cannot Be Openend")

    # Clean Up Data from links
    def _clean_data(self, lines):
        c_lines = []
        for i in range(len(lines)):
            line = lines[i]
            c_lines.append(re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', line))

        return c_lines
    
    # TfIdf Algorythms
    def 
if __name__ == "__main__":
    tfIdf = TfIdf()
    tfIdf._load_data()