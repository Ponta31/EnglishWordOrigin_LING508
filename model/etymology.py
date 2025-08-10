#from model.morpheme import *

class Etymology:
    def __init__(self,
                 id: str,
                 origin_and_history: str):
        if not origin_and_history:
            raise ValueError("origin_and_history cannot be None")

        self.id = id
        self.origin_and_history = origin_and_history



