from injector import inject

from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilSpeechNum import GameVilSpeechNum
from pywolfbbs.domain.GameVil.value.GameVilSpeechPt import GameVilSpeechPt
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo
from pywolfbbs.infrastructure.repository.VilMember.VilMemberDateStateRepository import VilMemberDateStateRepository


class VilMemberDateState:
    """
    @DomainObject 村参加者の日ごとの状態
    @EntityObject （一意性のある）村（ゲーム）の参加者の日ごとの状態を表す
    """

    @inject
    def __init__(self, r: VilMemberDateStateRepository):
        self.repository = r
        self.vil_no = None
        self.member_no = None
        self.date_num = None    # 日数
        self.place = None   # 居場所（地上／墓下／見学）
        self.remain_speech_num = None   # 残り発言数
        self.remain_speech_pt = None    # 残り発言Pt
        self.vote_member = None  # 投票相手（参加者）
        self.use_ability_member = None    # 能力行使相手（参加者）

    def setValues(self, no: GameVilNo, member_no: VilMemberNo, date: GameVilDateNum,
                  num: GameVilSpeechNum, pt: GameVilSpeechPt, vote: VilMemberNo, use_abi: VilMemberNo):
        """
        セッターメソッド
        :param no:
        :param member_no:
        :param date:
        :param num:
        :param pt:
        :param vote:
        :param use_abi:
        :return:
        """
        self.vil_no = no
        self.member_no = member_no
        self.date_num = date
        self.remain_speech_num = num
        self.remain_speech_pt = pt
        self.vote_member = vote
        self.use_ability_member = use_abi

    def setValuesByRepository(self) -> None:
        """
        DB取得値をセット
        :return: なし
        """
        state = self.repository.queryVilMemberDateState(
            self.vil_no.getValue(), self.member_no.getValue(), self.date_num.getValue())

        self.remain_speech_num = GameVilSpeechNum(int(state[0]))
        self.remain_speech_pt = GameVilSpeechPt(int(state[1]))

        if state[2] is not None:
            self.vote_member = VilMemberNo(int(state[2]))

        if state[3] is not None:
            self.use_ability_member = VilMemberNo(int(state[3]))

    def createVilMemberDateState(self) -> int:
        """
        村参加者の日ごとの状態を作成
        :param self:
        :return:
        """

    # 永続化

    # 残り発言数を減らす

    # 残りpt数を減らす

    # 投票先をセット

    # 能力行使先をセット