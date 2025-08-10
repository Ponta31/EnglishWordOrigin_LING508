from typing import List
from model.meaning import Meaning
from model.etymology import Etymology
from model.morpheme import Morpheme
from model.pronunciation import Pronunciation

class LexicalEntry:
    def __init__(self,
                 id: int,
                 lemma_form: str,
                 meaning: Meaning,
                 pronunciation: Pronunciation,
                 etymology: Etymology,
                 morphemes: List[Morpheme]):

        if not lemma_form:
            raise ValueError("lemma_form cannot be None")

        self.id = id
        self.lemma_form = lemma_form
        self.meaning = meaning
        self.pronunciation = pronunciation
        self.etymology = etymology
        self.morphemes = morphemes



