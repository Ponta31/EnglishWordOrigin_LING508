from typing import List


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


class Meaning:
    def __init__(self,
                 id: int,
                 definition: str,
                 pos: PartOfSpeech,
                 example_sentence: str):

        if not definition:
            raise ValueError("definition cannot be None")
        if not isinstance(pos, PartOfSpeech):
            raise TypeError("pos must be a PartOfSpeech instance")

        self.id = id
        self.definition = definition
        self.pos = pos
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

