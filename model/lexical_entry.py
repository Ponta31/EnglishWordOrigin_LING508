from typing import List
from model.common_enums import *


class Meaning:
    def __init__(self,
                 id: int,
                 pos: PartOfSpeech,
                 definition: str,
                 example_sentence: str):

        if not definition:
            raise ValueError("definition cannot be None")
        if not isinstance(pos, PartOfSpeech):
            raise TypeError("pos must be a PartOfSpeech instance")

        self.id = id
        self.pos = pos
        self.definition = definition
        self.example_sentence = example_sentence


class Pronunciation:
    def __init__(self, lexical_entry_id: int, ipa: str):
        if not isinstance(ipa, str):
            raise TypeError("ipa must be a string")
        self.lexical_entry_id = lexical_entry_id
        self.ipa = ipa



class Etymology:
    def __init__(self,
                 id: str,
                 origin: str):
        if not origin:
            raise ValueError("origin cannot be None")

        self.id = id
        self.origin = origin




class Morpheme:
    def __init__(self,
                 id: str,
                 form: str,
                 gloss: str):
        if not form:
            raise ValueError("morpheme cannot be None")
        if not gloss:
            raise ValueError("meaning cannot be None")

        self.id = id
        self.form = form
        self.gloss = gloss





class LexicalEntry:
    def __init__(self,
                 id: int,
                 lemma_form: str,
                 meaning: List[Meaning],
                 pronunciation: Pronunciation,
                 etymology: List[Etymology],
                 morphemes: List[Morpheme]):

        if not lemma_form:
            raise ValueError("lemma_form cannot be None")

        self.id = id
        self.lemma_form = lemma_form
        self.meaning = meaning
        self.pronunciation = pronunciation
        self.etymology = etymology
        self.morphemes = morphemes


#about json https://stackoverflow.com/questions/63893843/how-to-convert-nested-object-to-nested-dictionary-in-python

    def get_json(self) -> dict:
        json = {
            "id": self.id,
            "lemma_form": self.lemma_form,
            "meaning": [
                {"id": m.id,
                 "pos": ,
                 "definition": m.definition,
                 "example_sentence": m.example_sentence
                } for m in self.meaning
            ],
            "pronunciation": {
                "ipa": self.pronunciation.ipa,
                }
            "etymology": [
                {"id": e.id,
                 "origin": e.origin
                 } for e in self.etymology
            ]
            "morphemes":

'''class Pronunciation:
    def __init__(self, lexical_entry_id: int, ipa: str):
        if not isinstance(ipa, str):
            raise TypeError("ipa must be a string")
        self.lexical_entry_id = lexical_entry_id
        self.ipa = ipa'''
