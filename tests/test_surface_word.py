from model.surface_word import *
from model.lexical_entry import *

def test_surface_word():
    lex_entry = LexicalEntry(lemma_form='revoke')
    word = SurfaceWord(surface_form='revoked', lex_entry=lex_entry)

    assert word.surface_form == 'revoked'
    assert word.lex_entry == lex_entry

