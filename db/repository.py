import abc
from abc import abstractmethod
from model.lexical_entry import LexicalEntry
from model.common_enums import PartOfSpeech
from model.meaning import Meaning

class AbstractRepository(metaclass=abc.ABCMeta):

    @abstractmethod
    def load_lexicon(self) -> list[LexicalEntry]:
        raise NotImplementedError()


