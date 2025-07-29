from model.common_enums import PartOfSpeech


class Meaning:
    def __init__(self, definition: str, pos: PartOfSpeech, example_sentence: str):
        if not definition:
            raise ValueError("definition cannot be None")
        if not isinstance(pos, PartOfSpeech):
            raise TypeError("pos must be a PartOfSpeech instance")


        self.definition = definition
        self.pos = pos
        self.example_sentence = example_sentence


