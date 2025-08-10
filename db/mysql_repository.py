from db.repository import *
import mysql.connector


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


# I may separately return meanings, pronunciation, etymology, morphemes in the future
    def _get_meaning(self, lexical_entry_id):
        sql = ("SELECT id, difinition, pos, example_sentence "
               "FROM meanings "
               "WHERE lexical_entry_id = %s ")
        self.cursor.execute(sql, lexical_entry_id)
        rows = self.cursor.fetchall()
        return [Meaning(id=row[0],
                        definition=row[1],
                        pos=PartOfSpeech(row[2]),
                        example_sentence=row[3])
                for row in rows]

    def _get_pronunciation(self, lexical_entry_id):
        sql = ("SELECT ipa")

    def _get_etymology(self, lexical_entry_id):
        sql = ("SELECT id, origin_and_history "
               "FROM etymology "
               "WHERE lexical_entry_id = %s ")
        self.cursor.execute(sql, lexical_entry_id)
        rows = self.cursor.fetchall()
        return [Etymology(id=row[0],
                          origin_and_history=row[1])
                for row in rows]

    def _get_morphemes(self, lexical_entry_id):
        sql = ("SELECT id, form, meaning "
               "FROM morpheme "
               "WHERE lexical_entry_id = %s ")
        self.cursor.execute(sql, (lexical_entry_id,))
        rows = self.cursor.fetchall()
        return [Morpheme(id=row[0],
                         form=row[1],
                         meaning=row[2])
                for row in rows
        ]


    # For public
    def load_lexicon(self):
        sql = ("SELECT lemma_form "
               "FROM lexical_entry "
               "JOIN meanings m ON le.id = m.lexical_entry_id"
               )
        self.cursor.execute(sql)
        entries = self.cursor.fetchall()
        lemma_forms = [row[0] for row in entries]

        lexicon = []
        for entry_id, lemma_form in entries:
            meanings = self.map_meanings(lemma_form)
            entry = LexicalEntry(row[0], row[1])
            lexicon.append(lex_entry)
        return lexicon

