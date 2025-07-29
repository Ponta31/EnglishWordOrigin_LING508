
class Root:
    def __init__(self, morpheme: str, meaning: str):
        if not morpheme:
            raise ValueError("morpheme cannot be None")
        if not meaning:
            raise ValueError("meaning cannot be None")

        self.morpheme = morpheme
        self.meaning = meaning

