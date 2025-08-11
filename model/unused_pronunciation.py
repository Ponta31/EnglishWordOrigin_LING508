
class Pronunciation:
    def __init__(self, lexical_entry_id: int, ipa: str):
        if not isinstance(ipa, str):
            raise TypeError("ipa must be a string")
        self.lexical_entry_id = lexical_entry_id
        self.ipa = ipa
