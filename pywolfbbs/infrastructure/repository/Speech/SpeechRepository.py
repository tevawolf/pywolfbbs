from abc import ABCMeta, abstractmethod
from datetime import datetime


class SpeechRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def addSpeech(self, name: str, dt: datetime, title: str, text: str, vil_no: int) -> bool:
        """
        BSpeechを永続化するメソッド
        :param vil_no:
        :param title:
        :param text:
        :param dt:
        :param name:
        :return:
        """
        pass
