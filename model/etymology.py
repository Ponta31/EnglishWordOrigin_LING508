from model.root import *

class Etymology:
    def __init__(self, origin_and_history: str, roots: list[Root] =None):
        if not origin_and_history:
            raise ValueError("origin_and_history cannot be None")
        if not isinstance(roots, list):
            raise TypeError("roots must be a list")


        self.origin_and_history = origin_and_history
        self.roots = roots



