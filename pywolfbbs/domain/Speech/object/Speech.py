from injector import inject

from pywolfbbs.domain.GameVil.value.GameVliNo import GameVliNo
from pywolfbbs.infrastructure.repository.Speech.SpeechRepository import SpeechRepository
from pywolfbbs.domain.Speech.value.SpeechText import SpeechText
from pywolfbbs.domain.Speech.value.SpeechNo import SpeechNo
from pywolfbbs.domain.Speech.value.PostDateTime import PostDateTime
from pywolfbbs.domain.Player.value.PlayerName import PlayerName


class Speech:
    """
    @DomainObject 発言
    @EntityObject （一意性のある）発言を表す
    """

    @inject
    def __init__(self, r: SpeechRepository):
        self.repository = r
        self.speechNo = None
        self.playerName = None
        self.postDateTime = None
        self.speechText = None
        self.vil_no = None

    def setValues(self, no: SpeechNo, name: PlayerName, dt: PostDateTime, text: SpeechText, thread_no: GameVliNo):
        self.speechNo = no
        self.playerName = name
        self.postDateTime = dt
        self.speechText = text
        self.vil_no = thread_no

    def createSpeach(self) -> None:
        """
        発言を作成
        :return: なし
        """
        # 永続化
        self.repository.addSpeech(
            self.playerName.getValue(),
            self.postDateTime.getValue(),
            self.speechText.getValue(),
            self.vil_no.getValue()
        )
