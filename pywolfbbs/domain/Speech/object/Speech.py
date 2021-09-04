from injector import inject

from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
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
        self.speech_no = None
        self.post_datetime = None
        self.speech_text = None
        self.player_id = None
        self.vil_no = None
        self.vil_date = None
        self.member = None

    def setValues(self, no: SpeechNo, dt: PostDateTime, text: SpeechText, player_id: PlayerId, vil_no: GameVilNo,
                  vil_date: GameVilDateNum):
        self.speech_no = no
        self.post_datetime = dt
        self.speech_text = text
        self.player_id = player_id
        self.vil_no = vil_no
        self.vil_date = vil_date

    def createSpeech(self) -> None:
        """
        発言を作成
        :return: なし
        """
        # 永続化
        self.repository.addSpeech(
            self.post_datetime.getValue(),
            self.speech_text.getValue(),
            self.player_id.getValue(),
            self.vil_no.getValue(),
            self.vil_date.getValue()
        )
