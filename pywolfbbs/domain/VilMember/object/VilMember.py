from injector import inject

from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.VilMember.value.VilMemberName import VilMemberName
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo
from pywolfbbs.domain.VilMember.value.VilMemberTitle import VilMemberTitle
from pywolfbbs.infrastructure.repository.VilMember.VilMemberRepository import VilMemberRepository


class VilMember:
    """
    @DomainObject 村参加者
    @EntityObject （一意性のある）村（ゲーム）の参加者を表す
    """

    @inject
    def __init__(self, r: VilMemberRepository):
        self.repository = r
        self.vil_no = None
        self.player_id = None
        self.member_no = None
        self.member_name = None
        self.member_title = None   # 肩書き
        self.chartip = None # キャラチップ
        self.alive = None   # 生死
        self.hope_position = None   # 希望役職
        self.position = None    # 役職

    def setValues(self, vil_no: GameVilNo, player_id: PlayerId, member_no: VilMemberNo, name: VilMemberName,
                  title: VilMemberTitle):
        self.vil_no = vil_no
        self.player_id = player_id
        self.member_no = member_no
        self.member_name = name
        self.member_title = title

    def setValuesByRepository(self) -> None:
        """
        DB取得値をセット
        :return: なし
        """
        member = self.repository.queryVilMember(self.vil_no.getValue(), self.player_id.getValue())

        if member:
            self.member_no = VilMemberNo(int(member[0]))
            self.member_name = VilMemberName(member[1])
            self.member_title = VilMemberTitle(member[2])

    def isMember(self) -> bool:
        """
        有効な参加者情報か
        :return: 有効／無効
        """
        return self.member_no.isNotZero()

    def createMember(self) -> None:
        """
        村の参加者を生成
        :return: 
        """
        self.repository.addMember(
            self.vil_no.getValue(),
            self.player_id.getValue(),
            self.member_name.getValue(),
            self.member_title.getValue()
        )

