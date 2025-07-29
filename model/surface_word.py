from model.lexical_entry import *

class SurfaceWord:
    def __init__(self, surface_form: str, lex_entry: LexicalEntry):
        if not surface_form:
            raise ValueError("surface_form cannot be None")
        if not isinstance(lex_entry, LexicalEntry):
            raise TypeError("lex_entry must be a LexicalEntry instance")

        self.surface_form = surface_form
        self.lex_entry = lex_entry

