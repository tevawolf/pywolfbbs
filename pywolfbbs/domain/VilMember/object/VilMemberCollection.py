import copy

from injector import inject

from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.VilMember.factory.VilMemberFactory import VilMemberFactory
from pywolfbbs.domain.VilMember.object.VilMember import VilMember
from pywolfbbs.infrastructure.repository.VilMember.VilMemberRepository import VilMemberRepository


class VilMemberCollection:
    """
    @CollectionObject 村参加のコレクション
    """
    @inject
    def __init__(self, r: VilMemberRepository):
        self.repository = r
        self.vil_no = None
        self.vil_members = []

    def setValues(self, vil_no: GameVilNo):
        """
        セッターメソッド
        :param vil_no:
        :return: なし
        """
        self.vil_no = vil_no

    def setVilMemberList(self):
        """
        リポジトリから村参加者のリストを取得し、保持する
        :return: なし
        """
        member_list = self.repository.queryVilMemberList(self.vil_no.getValue())
        for m in member_list:
            member = VilMemberFactory.create(m[0], m[1], m[2], m[3], m[4], m[5])
            self.vil_members.append(member)

    def listAllMembers(self) -> [VilMember]:
        """
        村の参加者をすべて提示する
        :return　村参加者リストのコピー
        """
        return copy.deepcopy(self.vil_members)
