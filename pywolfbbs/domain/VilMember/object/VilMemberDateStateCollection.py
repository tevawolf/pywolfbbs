import copy

from injector import inject

from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.VilMember.factory.VilMemberDateStateFactory import VilMemberDateStateFactory
from pywolfbbs.domain.VilMember.object.VilMemberDateState import VilMemberDateState
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo
from pywolfbbs.infrastructure.repository.VilMember.VilMemberDateStateRepository import VilMemberDateStateRepository


class VilMemberDateStateCollection:
    """
    @CollectionObject 村参加者のその日の状態のコレクション
    """
    @inject
    def __init__(self, r: VilMemberDateStateRepository):
        self.repository = r
        self.vil_no = None
        self.member_no = None
        self.date_num = None
        self.vil_members_date_state = []

    def setValues(self, vil_no: GameVilNo, member_no: VilMemberNo, date_num: GameVilDateNum):
        """
        セッターメソッド
        :param vil_no:
        :param member_no:
        :param date_num
        :return: なし
        """
        self.vil_no = vil_no
        self.member_no = member_no
        self.date_num = date_num

    def setVilMemberDateStateListByDate(self):
        """
        リポジトリから村参加者のその日の状態リストを取得し、保持する
        :return: なし
        """
        member_list = self.repository.queryVilMemberDateStateDateList(self.vil_no.getValue(), self.date_num.getValue())
        for m in member_list:
            vote = None
            use = None
            if m[3] is not None:
                vote = int(m[3])
            if m[4] is not None:
                use = int(m[4])

            member = VilMemberDateStateFactory.create(self.vil_no.getValue(), int(m[0]), self.date_num.getValue(),
                                                      int(m[1]), int(m[2]), vote, use)
            self.vil_members_date_state.append(member)

    def listAllMembersState(self) -> [VilMemberDateState]:
        """
        村の参加者のその日の状態をすべて提示する
        :return　村参加者の状態リストのコピー
        """
        return copy.deepcopy(self.vil_members_date_state)
