
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

