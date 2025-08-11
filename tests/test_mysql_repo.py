from db.mysql_repository import *
from model.lexical_entry import Etymology

repo = MySQLRepository()


'''
entry = LexicalEntry(id=le_id,
                     lemma_form=le_form,
                     meaning=meaning,
                     pronunciation=pronunciation,
                     etymology=etymology,
                     morphemes=morphemes)

'''

"""
#Check all meaning/meanings/definition

TABLE meanings (
    id INT AUTO_INCREMENT,
    lexical_entry_id INT NOT NULL,
    pos ENUM('verb', 'noun', 'adjective'),
    definition NVARCHAR(150),
    example_sentence VARCHAR(150),
    PRIMARY KEY (id),
    FOREIGN KEY (lexical_entry_id) REFERENCES lexical_entry(id)
);

INSERT INTO meanings
    (lexical_entry_id, pos, definition, example_sentence)
VALUES
    (1, 'adjective', N'突然の', 'The car came to an abrupt stop.'),
    (2, 'verb', N'正式に取り消す', 'The government decided to revoke the license.'),
    (3, 'verb', N'遊ぶ、演奏する', 'The children play in the park.'),
    (3, 'noun', N'演劇、遊び', 'They watched a play at the theater.');
;

    class Meaning:
    def __init__(self,
                 id: int,
                 definition: str,
                 pos: PartOfSpeech,
                 example_sentence: str):

        if not definition:
            raise ValueError("definition cannot be None")
        if not isinstance(pos, PartOfSpeech):
            raise TypeError("pos must be a PartOfSpeech instance")

        self.id = id
        self.definition = definition
        self.pos = pos
        self.example_sentence = example_sentence


    def _get_meaning(self, lexical_entry_id):
        sql = ("SELECT id, pos, definition, example_sentence "
               "FROM meanings "
               "WHERE lexical_entry_id = %s ORDER BY id")
        self.cursor.execute(sql, (lexical_entry_id,))
        rows = self.cursor.fetchall()
        return [Meaning(id=row[0],
                        pos=self._map_pos(row[1]),
                        definition=row[2],
                        example_sentence=row[3],)
                for row in rows]



 def load_lexicon(self) -> List[LexicalEntry]:
        sql = ("SELECT id, lemma_form "
               "FROM lexical_entry "
               )
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        lexicon = []
        for le_id, le_form in rows:

            meaning = self._get_meaning(le_id)
            pronunciation = self._get_pronunciation(le_id)
            etymology = self._get_etymology(le_id)
            morphemes = self._get_morphemes(le_id)

            entry = LexicalEntry(id=le_id,
                                 lemma_form=le_form,
                                 meaning=meaning,
                                 pronunciation=pronunciation,
                                 etymology=etymology,
                                 morphemes=morphemes)

            lexicon.append(entry)
        return lexicon


    def get_entry(self, lemma_form: str) -> LexicalEntry:
        sql = ("SELECT id, lemma_form "
               "FROM lexical_entry "
               "WHERE lemma_form = %s ")
        self.cursor.execute(sql, (lemma_form,))
        row = self.cursor.fetchone()

        le_id, le_form = row

        meaning = self._get_meaning(le_id)
        pronunciation = self._get_pronunciation(le_id)
        etymology = self._get_etymology(le_id)
        morphemes = self._get_morphemes(le_id)

        entry = LexicalEntry(id=le_id,
                             lemma_form=le_form,
                             meaning=meaning,
                             pronunciation=pronunciation,
                             etymology=etymology,
                             morphemes=morphemes)
        return entry
        
        
        

class LexicalEntry:
    def __init__(self,
                 id: int,
                 lemma_form: str,
                 meaning: List[Meaning],
                 pronunciation: Pronunciation,
                 etymology: List[Etymology],
                 morphemes: List[Morpheme]):

        if not lemma_form:
            raise ValueError("lemma_form cannot be None")

        self.id = id
        self.lemma_form = lemma_form
        self.meaning = meaning
        self.pronunciation = pronunciation
        self.etymology = etymology
        self.morphemes = morphemes



"""





def test_get_entry():
    entry = repo.get_entry('play')
    assert isinstance(entry, LexicalEntry)
    assert entry.lemma_form == 'play'

    defs = [m.definition for m in entry.meaning]
    assert isinstance(defs, list)
    assert '遊ぶ、演奏する' in defs
    assert '演劇、遊び' in defs




def test_load_lexicon():
    lexicon = repo.load_lexicon()
    assert isinstance(lexicon, list)

    lemmas = {le.lemma_form for le in lexicon}
    assert "abrupt" in lemmas


