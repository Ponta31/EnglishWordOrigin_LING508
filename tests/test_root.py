from model.root import *

def test_root():
    root = Root(morpheme='re', meaning='again')

    assert root.morpheme == 're'
    assert root.meaning == 'again'

