from injector import inject

from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.Speech.enum.SpeechType import SpeechType
from pywolfbbs.domain.VilMember.value.VilMemberName import VilMemberName
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo
from pywolfbbs.domain.VilMember.value.VilMemberTitle import VilMemberTitle
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
        self.speech_type = None
        self.speech_text = None
        self.player_id = None
        self.vil_no = None
        self.vil_date = None
        self.member_no = None
        self.member_title = None   # 肩書き（発言時）
        self.member_name = None   # 名前（発言時）

    def setValues(self, no: SpeechNo, dt: PostDateTime, type: SpeechType, text: SpeechText, player_id: PlayerId,
                  vil_no: GameVilNo, vil_date: GameVilDateNum,
                  member_no: VilMemberNo, member_title: VilMemberTitle, member_name: VilMemberName):
        self.speech_no = no
        self.post_datetime = dt
        self.speech_type = type
        self.speech_text = text
        self.player_id = player_id
        self.vil_no = vil_no
        self.vil_date = vil_date
        self.member_no = member_no
        self.member_title = member_title
        self.member_name = member_name

    def createSpeech(self, conn) -> None:
        """
        発言を作成
        :return: なし
        """
        # 永続化
        self.repository.addSpeech(conn,
            self.post_datetime.getValue(),
            self.speech_type.value,
            self.speech_text.getValue(),
            self.player_id.getValue(),
            self.vil_no.getValue(),
            self.vil_date.getValue(),
            self.member_no.getValue(),
            self.member_title.getValue(),
            self.member_name.getValue()
        )
