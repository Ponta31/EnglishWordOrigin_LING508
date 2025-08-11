import pytest
from app.services import *
from db.mysql_repository import *

services = Services()
repo = MySQLRepository()

'''    entry = LexicalEntry(id=le_id,
                             lemma_form=le_form,
                             meaning=meaning,
                             pronunciation=pronunciation,
                             etymology=etymology,
                             morphemes=morphemes)
        return entry
'''
'''     
        Meaning
        self.id = id
        self.pos = pos
        self.definition = definition
        self.example_sentence = example_sentence'''


def test_lookup_word():
    info = services.lookup_word('revoked')
    assert info["lemma_form"] == "revoke"
    assert info["meaning"][0]["pos"] == "verb"
    assert info["pronunciation"]["ipa"] == "rɪˈvoʊk"
    assert info["etymology"][0]["origin"].startswith("revokeの語源は")
    assert info["morphemes"][0]["gloss"] in ["again", "call"]

