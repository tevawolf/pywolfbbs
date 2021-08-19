from injector import inject

from pywolfbbs.domain.GameVil.value.GameVliNo import GameVliNo
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.infrastructure.repository.Speech.SpeechRepository import SpeechRepository
from pywolfbbs.domain.Speech.value.SpeechText import SpeechText
from pywolfbbs.domain.Speech.value.SpeechNo import SpeechNo
from pywolfbbs.domain.Speech.value.PostDateTime import PostDateTime


class Speech:
    """
    @DomainObject 発言
    @EntityObject （一意性のある）発言を表す
    """

    @inject
    def __init__(self, r: SpeechRepository):
        self.repository = r
        self.speechNo = None
        self.postDateTime = None
        self.speechText = None
        self.playerId = None
        self.vil_no = None

    def setValues(self, no: SpeechNo, dt: PostDateTime, text: SpeechText, player_id: PlayerId, vil_no: GameVliNo):
        self.speechNo = no
        self.postDateTime = dt
        self.speechText = text
        self.playerId = player_id
        self.vil_no = vil_no

    def createSpeach(self) -> None:
        """
        発言を作成
        :return: なし
        """
        # 永続化
        self.repository.addSpeech(
            self.postDateTime.getValue(),
            self.speechText.getValue(),
            self.playerId.getValue(),
            self.vil_no.getValue()
        )
