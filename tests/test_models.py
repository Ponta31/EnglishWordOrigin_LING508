from model.lexical_entry import *
from model.common_enums import *
from model.surface_word import *

def test_etymology_and_morph():
    morph1 = Morpheme(id=1, form='re', gloss='again')
    morph2 = Morpheme(id=2, form='vok', gloss='call')

    etym = Etymology(
        id=10,
        origin= "revokeの語源は(re + vocare)"
    )

    assert etym.origin.startswith("revokeの語源は")
    assert morph1.form == 're'
    assert morph1.gloss == 'again'
    assert len(morph2.form) == 3


def test_meaning():

    meaning = Meaning(
        id="2",
        definition='正式に取り消す',
        pos=PartOfSpeech.VERB,
        example_sentence="The administration revoked students' visas."
    )

    assert meaning.definition == '正式に取り消す'
    assert meaning.pos == PartOfSpeech.VERB
    assert meaning.example_sentence == "The administration revoked students' visas."




def test_part_of_speech():
    assert PartOfSpeech.VERB.name == 'VERB'
    assert PartOfSpeech.ADJECTIVE.value == 'adjective'


def test_pronunciation():
    pron = Pronunciation(lexical_entry_id=2, ipa='rɪˈvoʊk')
    assert pron.ipa == 'rɪˈvoʊk'


'''
class LexicalEntry:
    def __init__(self,
                 id: int,
                 lemma_form: str,
                 meaning: List[Meaning],
                 pronunciation: Pronunciation,
                 etymology: List[Etymology],
                 morphemes: List[Morpheme]):
'''


def test_surface_word():
    lex_entry = LexicalEntry(lemma_form='revoke')
    word = SurfaceWord(surface_form='revoked', lex_entry=lex_entry)

    assert word.surface_form == 'revoked'
    assert word.lex_entry == lex_entry





'''


def test_mnemonic():

    mnemonic = Mnemonic(
        ja_sentence='油ぷっと噴き出す',
        sentence_vector=[0.2, 0.3, 0.1],
        similarity_to_lemma=0.77
    )

    assert mnemonic.ja_sentence == '油ぷっと噴き出す'
    assert isinstance(mnemonic.sentence_vector, list)
    assert mnemonic.similarity_to_lemma > 0.7
'''













