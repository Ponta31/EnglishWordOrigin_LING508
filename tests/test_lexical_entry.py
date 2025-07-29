from model.lexical_entry import *

def test_lexical_entry():
    le = LexicalEntry(lemma_form='revoke', same_root_entries=[])

    assert le.lemma_form == 'revoke'
    assert le.same_root_entries == []

