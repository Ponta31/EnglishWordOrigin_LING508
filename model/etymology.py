from model.morpheme import *

class Etymology:
    def __init__(self, origin_and_history: str):
        if not origin_and_history:
            raise ValueError("origin_and_history cannot be None")



        self.origin_and_history = origin_and_history



