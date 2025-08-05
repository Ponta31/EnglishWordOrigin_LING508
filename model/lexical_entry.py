from model.meaning import Meaning
from model.etymology import Etymology
from model.pronunciation import Pronunciation

class LexicalEntry:
    def __init__(self,
                 lemma_form: str,
                 meanings: str = None,
                 pronunciation: Pronunciation = None,
                 etymology: Etymology = None):
        if not lemma_form:
            raise ValueError("lemma_form cannot be None")

        self.lemma_form = lemma_form
        self.meanings = meanings
        self.pronunciation = pronunciation
        self.etymology = etymology



