from datetime import datetime

from pywolfbbs.domain.Speech.factory.SpeechCollectionFactory import SpeechCollectionFactory
from pywolfbbs.domain.Speech.factory.SpeechFactory import SpeechFactory
from pywolfbbs.domain.Speech.object.SpeechCollection import SpeechCollection


class SpeechService:
    """
    発言のサービスオブジェクト
    """

    @staticmethod
    def getSpeeches(no: int, disp_date: int) -> SpeechCollection:
        """
        村番号・日付に該当する発言を取得
        FIXME 今後はページングやフィルタリングに対応させる
        :param no:
        :param disp_date:
        :return:
        """
        speeches = SpeechCollectionFactory.create(no)
        speeches.setSpeechList(disp_date)

        return speeches

    @staticmethod
    def postSpeech(dt: datetime, text: str, player_id: str, vil_no: int, vil_date: int,
                   member_title: str, member_name: str) -> None:
        """
        発言投稿
        :param dt:
        :param text:
        :param player_id:
        :param vil_no:
        :param vil_date:
        :param member_title:
        :param member_name:
        :return:
        """

        speech = SpeechFactory.create(9999, dt, text, player_id, vil_no, vil_date, member_title, member_name)
        speech.createSpeech()
