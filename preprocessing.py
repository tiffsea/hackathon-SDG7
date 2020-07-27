from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

class preprocessing():

    def __init__(self, t):
        self.all_stopwords = stopwords.words('english')
        self.punc = string.punctuation
        self.get_tokens(t)

    def get_tokens(self, text):
        word_toks = word_tokenize(text)
        tokens_without_sw = [word for word in word_toks if not word in self.all_stopwords]
        tokens_without_punc = [word for word in tokens_without_sw if not word in self.punc]
        tokens_lower = [word.lower() for word in tokens_without_punc]
        tokens_no_nums = [word for word in tokens_lower if word.isalpha()]
        return tokens_no_nums
