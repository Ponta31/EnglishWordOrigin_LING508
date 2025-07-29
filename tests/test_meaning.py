from model.meaning import *
from model.common_enums import *

def test_meaning():

    meaning = Meaning(
        definition='取り消す',
        pos=PartOfSpeech.VERB,
        example_sentence="The administration revoked a student's visa."
    )

    assert meaning.definition == '取り消す'
    assert meaning.pos == PartOfSpeech.VERB
    assert meaning.example_sentence == "The administration revoked students' visas."

