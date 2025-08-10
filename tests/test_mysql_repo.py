from db.mysql_repository import *


repo = MySQLRepository()


def test_map_pos():
    assert repo.map_pos("verb") == PartOfSpeech.VERB
    assert repo.map_pos("noun") == PartOfSpeech.NOUN


def test_map_meanings():
    meanings = repo.map_meanings('play')
    assert isinstance(meanings, list)
    assert '遊ぶ、演奏する' in meanings
    assert '演劇、遊び' in meanings



def test_load_lexicon():
    lexicon = repo.load_lexicon()
    assert isinstance(lexicon, list)


