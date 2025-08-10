
class Morpheme:
    def __init__(self,
                 id: str,
                 form: str,
                 meaning: str):
        if not form:
            raise ValueError("morpheme cannot be None")
        if not meaning:
            raise ValueError("meaning cannot be None")

        self.id = id
        self.form = form
        self.meaning = meaning

