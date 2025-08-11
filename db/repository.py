import abc
from abc import abstractmethod
from model.lexical_entry import LexicalEntry
from model.common_enums import PartOfSpeech



class AbstractRepository(metaclass=abc.ABCMeta):


    #Return all words entries
    @abstractmethod
    def load_lexicon(self) -> list[LexicalEntry]:
        raise NotImplementedError()

    #Return a single word LexicalEntry
    @abstractmethod
    def get_entry(self, lemma_form: str) -> LexicalEntry:
        raise NotImplementedError()


