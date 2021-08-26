from datetime import datetime

from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.Speech.factory.SpeechFactory import SpeechFactory
from pywolfbbs.domain.GameVil.factory.GameVliFactory import GameVliFactory
from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel


class GameVilService:
    """
    村表示
    発言投稿
    パスワード認証
    """

    @staticmethod
    def displayVil(no: int, disp_date: int) -> GameVil:
        # 公開レベル、現在日、現在日ステータスもダミー
        vil = GameVliFactory.create(no, 'dummy', GameVilPublicLevel.公開, 'dummy', 0, GameVilDateStatus.プロローグ)
        vil.setValuesByRepository()
        vil.setVilDateList()
        vil.setSpeechList(disp_date)
        return vil

    @staticmethod
    def postSpeech(dt: datetime, text: str, player_id: str, vil_no: int, vil_date: int) -> None:

        speech = SpeechFactory.create(9999, dt, text, player_id, vil_no, vil_date)
        speech.createSpeach()

    @staticmethod
    def authenticatePassword(no: int, password: str) -> bool:
        # 公開レベル、現在日、現在日ステータスもダミー
        vil = GameVliFactory.create(no, 'dummy', GameVilPublicLevel.公開, password, 0, GameVilDateStatus.プロローグ)
        return vil.isPasswordMatched()
