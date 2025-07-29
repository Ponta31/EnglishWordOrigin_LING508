from model.pronunciation import *

def test_pronunciation():

    pron = Pronunciation(ipa='rɪˈvoʊk')

    assert pron.ipa == 'rɪˈvoʊk'