from model.mnemonic import *

def test_mnemonic():

    mnemonic = Mnemonic(
        ja_sentence='油ぷっと噴き出す',
        sentence_vector=[0.2, 0.3, 0.1],
        similarity_to_lemma=0.77
    )

    assert mnemonic.ja_sentence == '油ぷっと噴き出す'
    assert isinstance(mnemonic.sentence_vector, list)
    assert mnemonic.similarity_to_lemma > 0.7

