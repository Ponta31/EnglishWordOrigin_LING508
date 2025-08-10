
class Mnemonic:
    def __init__(self, ja_sentence: str, sentence_vector: list[float], similarity_to_lemma: float):
        if not ja_sentence:
            raise ValueError("ja_sentence cannot be None")
        if not isinstance(sentence_vector, list):
            raise TypeError("sentence_vector must be a list")

        self.ja_sentence = ja_sentence
        self.sentence_vector = sentence_vector
        self.similarity_to_lemma = similarity_to_lemma
