import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')

class Lexical:
    def __init__(self,text):
        self.text = text

    def get_verbs(self):
        words = word_tokenize(self.text)
        tagged_words = pos_tag(words)  # etiketleme, bu özne bu yüklem vs
        verbs = [words for word,tag in tagged_words if tag.startswith('VB')] # kontrol edip vb ile başlayanları verbse at kelimeleri
        return verbs