from model.morpheme import *

def test_root():
    morph = Morpheme(form='re', meaning='again')

    assert morph.form == 're'
    assert morph.meaning == 'again'

