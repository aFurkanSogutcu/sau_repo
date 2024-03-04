import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy

nltk.download('averaged_perceptron_tagger')
nlp = spacy.load('en_core_web_sm')

class Lexical:
    def __init__(self,text):
        self.text = text

    def get_verbs(self):
        words = word_tokenize(self.text)
        tagged_words = pos_tag(words)  # etiketleme, bu özne bu yüklem vs
        verbs = [words for word,tag in tagged_words if tag.startswith('VB')] # kontrol edip vb ile başlayanları verbse at kelimeleri
        return verbs

    def get_pople_names(self):
        doc = nlp(self.text)
        name = [entity.text for entity in doc.entities if entity.label_ == "PERSON"] # isimleri getirir

        