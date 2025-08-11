import db.mysql_repository


class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MySQLRepository()

    def lookup_word(self, surface_form: str):

        #if there is no input(surface form)
        if not surface_form:
            raise ValueError("Input is required")

        #if there is no word in inflected_form
        lemma = self.repo.lemmatize(surface_form)
        if not lemma:
            return {"error": f"No lemma found {surface_form}"}


        #if it's conjugated word
        entry = self.repo.get_entry(lemma)
        if entry:
            return entry.get_json()

        return {"error": f"No entry found {lemma}"}
