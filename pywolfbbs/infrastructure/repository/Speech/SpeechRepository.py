from abc import ABCMeta, abstractmethod
from datetime import datetime


class SpeechRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def querySpeechList(self, no: int, date: int) -> []:
        """
        Speechのリストを返すクエリーメソッド
        :return: Speechのリスト
        """
        return []

    @abstractmethod
    def addSpeech(self, conn, dt: datetime, type: int, text: str, player_id: str, vil_no: int, vil_date
                  , member_no: int, member_title: str, member_name: str) -> bool:
        """
        Speechを永続化するメソッド
        :param dt:　投稿日時
        :param type: 発言種別
        :param text: 発言の文面
        :param player_id:　プレイヤーID
        :param vil_no:　村番号
        :param vil_date: 村の日付（発言日付）
        :param member_no: 参加者番号
        :param member_title:　肩書き（発言時）
        :param member_name: 　名前（発言時）

        :return: 追加の成否
        """
        pass
