from db.repository import *
import mysql.connector
from model.lexical_entry import *


class MySQLRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

        #For local use
        config = {'user': 'root',
            	  'passwd': 'strongpassword',
                  'host': 'localhost',
                  'port': '32000',
                  'database': 'en_jp',
                  }

        """
        
        config = {'user': 'root',
            	  'passwd': 'strongpassword',
                  'host': 'mysql',
                  'port': '3306',
                  'database': 'en_jp'}
        """

        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


# Helpers_I may separately return meanings, pronunciation, etymology, morphemes in the future

    def _map_pos(self, pos_str) -> PartOfSpeech:
        pos_switcher = {'verb': PartOfSpeech.VERB,
                        'noun': PartOfSpeech.NOUN,
                        'adjective': PartOfSpeech.ADJECTIVE,
                        'adverb': PartOfSpeech.ADVERB,
                        'pronoun': PartOfSpeech.PRONOUN,
                        'preposition': PartOfSpeech.PREPOSITION}
        return pos_switcher.get(pos_str, None)

#meaning can be rows
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

#Pronunciation should be one row
    def _get_pronunciation(self, lexical_entry_id):
        sql = ("SELECT lexical_entry_id, ipa "
               "FROM pronunciation "
               "WHERE lexical_entry_id = %s ")
        self.cursor.execute(sql, (lexical_entry_id,))
        row = self.cursor.fetchone()
        return Pronunciation(lexical_entry_id=row[0],ipa=row[1])


#etymology may be rows
    def _get_etymology(self, lexical_entry_id):
        sql = ("SELECT id, origin "
               "FROM etymology "
               "WHERE lexical_entry_id = %s ")
        self.cursor.execute(sql, (lexical_entry_id,))
        rows = self.cursor.fetchall()
        return [Etymology(id=row[0],
                          origin=row[1])
                for row in rows]


#morphemes is rows

    def _get_morphemes(self, lexical_entry_id):
        sql = ("SELECT m.id, m.form, m.gloss "
               "FROM morpheme m "
               "JOIN etymology_morpheme em ON em.morpheme_id = m.id "
               "JOIN etymology e ON e.id = em.etymology_id "
               "WHERE e.lexical_entry_id = %s ORDER BY m.id")

        self.cursor.execute(sql, (lexical_entry_id,))
        rows = self.cursor.fetchall()
        return [Morpheme(id=row[0],
                         form=row[1],
                         gloss=row[2])
                for row in rows
        ]


# For public
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


    def lemmatize(self, surface_form: str) -> str:
        #Only SELECT lemma_form in the row
        sql = ("SELECT le.lemma_form "
               "FROM lexical_entry le "
               "JOIN inflected_forms f ON f.lexical_entry_id = le.id "
               "WHERE f.form = %s ")
        self.cursor.execute(sql, (surface_form,))
        row = self.cursor.fetchone()
        if row:
            return row[0]

        #If there is no inflected form, only lemma_form
        sql = ("SELECT lemma_form "
               "FROM lexical_entry "
               "WHERE lemma_form = %s ")
        self.cursor.execute(sql, (surface_form,))
        row = self.cursor.fetchone()
        if row:
            return row[0]

        #If there is no on the table
        return None

