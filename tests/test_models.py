from model.etymology import *
from model.lexical_entry import *
from model.meaning import *
from model.common_enums import *
from model.morpheme import *
from model.pronunciation import *
from model.surface_word import *
#from model.mnemonic import *

def test_etymology():
    morph1 = Morpheme(form='re', meaning='again')
    morph2 = Morpheme(form='voke', meaning='to call')

    etym = Etymology(
        origin_and_history= ("revokeの語源は、ラテン語の「revocare」に由来しています。この言葉は、「re-」（再、逆）と「vocare」（呼ぶ、呼び戻す）という二つの部分から成り立っています。「re-」は「戻す」という意味を持ち、「vocare」は「呼ぶ」という意味を持つため、合成すると「呼び戻す」や「再び呼ぶ」という意味になります。英語においては、revokeは、一度与えられた権利や許可を取り消すこと、または無効にすることを示しています。この概念は元々の語源に通じており、何かを再び呼び戻すというニュアンスが反映されています。したがって、法的な文脈や契約の取り消しに関してよく使われる言葉となっています。"
        )
    )

    assert etym.origin_and_history.startswith("revokeの語源は")
    assert morph1.form == 're'
    assert morph1.meaning == 'again'
    assert len(morph1.form) == 2







def test_lexical_entry():
    le = LexicalEntry(lemma_form='revoke', ) # removed same_root_entries=[]
    assert le.lemma_form == 'revoke'
    # assert le.same_root_entries == []








def test_meaning():

    meaning = Meaning(
        definition='取り消す',
        pos=PartOfSpeech.VERB,
        example_sentence="The administration revoked students' visas."
    )

    assert meaning.definition == '取り消す'
    assert meaning.pos == PartOfSpeech.VERB
    assert meaning.example_sentence == "The administration revoked students' visas."



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




def test_root():
    morph = Morpheme(form='re', meaning='again')

    assert morph.form == 're'
    assert morph.meaning == 'again'






from model.common_enums import *

def test_part_of_speech():
    assert PartOfSpeech.VERB.name == 'VERB'
    assert PartOfSpeech.ADJECTIVE.value == 'adjective'








def test_pronunciation():

    pron = Pronunciation(ipa='rɪˈvoʊk')

    assert pron.ipa == 'rɪˈvoʊk'







def test_surface_word():
    lex_entry = LexicalEntry(lemma_form='revoke')
    word = SurfaceWord(surface_form='revoked', lex_entry=lex_entry)

    assert word.surface_form == 'revoked'
    assert word.lex_entry == lex_entry








