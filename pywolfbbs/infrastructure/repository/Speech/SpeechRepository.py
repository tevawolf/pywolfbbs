from abc import ABCMeta, abstractmethod
from datetime import datetime


class SpeechRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def addSpeech(self,  dt: datetime, text: str, player_id: str, vil_no: int, vil_date: int) -> bool:
        """
        BSpeechを永続化するメソッド
        :param text: 発言の文面
        :param dt:　投稿日時
        :param player_id:　プレイヤーID
        :param vil_no:　村番号
        :param vil_date: 村の日付（発言日付）
        :return: 追加の成否
        """
        pass
