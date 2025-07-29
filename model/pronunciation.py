
class Pronunciation:
    def __init__(self, ipa: str):
        if not isinstance(ipa, str):
            raise TypeError("ipa must be a string")

        self.ipa = ipa
