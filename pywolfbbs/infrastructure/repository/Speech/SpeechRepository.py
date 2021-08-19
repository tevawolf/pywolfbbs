from abc import ABCMeta, abstractmethod
from datetime import datetime


class SpeechRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def addSpeech(self,  dt: datetime, text: str, player_id: str, vil_no: int) -> bool:
        """
        BSpeechを永続化するメソッド
        :param text:
        :param dt:
        :param player_id:
        :param vil_no:
        :return:
        """
        pass
