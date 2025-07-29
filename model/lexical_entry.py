

class LexicalEntry:
    def __init__(self, lemma_form: str, same_root_entries: list =None):
        if not lemma_form:
            raise ValueError("lemma_form cannot be None")

        self.lemma_form = lemma_form
        self.same_root_entries = same_root_entries

