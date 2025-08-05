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
                  'database': 'en_jp'}

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

    def map_pos(self, entry) -> PartOfSpeech:
        pos_switcher = {
            'verb': PartOfSpeech.VERB,
            'noun': PartOfSpeech.NOUN,
            'adjective': PartOfSpeech.ADJECTIVE,
        }
        return pos_switcher.get(entry)

    def map_meanings(self, lemma):
        sql = ("SELECT id "
               "FROM lexical_entry "
               "WHERE lemma_form LIKE %s"
               )
        self.cursor.execute(sql, (lemma,))
        row = self.cursor.fetchall()
        lexical_entry_id = row[0][0]

        sql = ("SELECT definition "
               "FROM meanings "
               "WHERE lexical_entry_id = %s "
               )
        self.cursor.execute(sql, (lexical_entry_id,))
        rows = self.cursor.fetchall()

        return [row[0] for row in rows]

    def load_lexicon(self):
        sql = ("SELECT le.lemma_form, m.definition "
               "FROM lexical_entry le "
               "JOIN meanings m ON le.id = m.lexical_entry_id"
               )
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        result = []
        for row in rows:
            entry = LexicalEntry(row[0], row[1])
            result.append(entry)
        return result

