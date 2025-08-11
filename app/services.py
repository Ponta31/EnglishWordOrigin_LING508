from db.mysql_repository import MySQLRepository


class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MySQLRepository()

    def lookup_word(self, surface_form: str):
