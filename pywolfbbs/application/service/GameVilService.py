from datetime import datetime

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
    def displayVil(no: int) -> GameVil:
        # 公開レベルもダミー
        vil = GameVliFactory.create(no, 'dummy', GameVilPublicLevel.公開, 'dummy')
        vil.setValuesByRepository()
        vil.setSpeechList()
        return vil

    @staticmethod
    def postSpeech(name: str, dt: datetime, title, text: str, thread_no: int) -> None:

        speech = SpeechFactory.create(9999, name, dt, title, text, thread_no)
        speech.createSpeach()

    @staticmethod
    def authenticatePassword(no: int, password: str) -> bool:
        # 公開レベルもダミー
        vil = GameVliFactory.create(no, 'dummy', GameVilPublicLevel.公開, password)
        return vil.isPasswordMatched()
