from pywolfbbs.domain.Organization.object.OrganizationPosition import OrganizationPosition
from pywolfbbs.domain.Position.value.PositionNo import PositionNo
from pywolfbbs.domain.VilMember.object.VilMember import VilMember
from pywolfbbs.domain.VilMember.object.VilMemberCollection import VilMemberCollection


class PositionMemberCollection:
    """
    @CollectionObject 村の役職単位の参加者コレクション
    """

    def __init__(self, position_no: PositionNo):
        self.position_no = position_no
        """役職No"""
        self.members = []
        """参加者リスト"""

    def setMembers(self, member_collection: VilMemberCollection):
        """
        渡された参加者コレクションから、このコレクションオブジェクトの役職と希望役職が一致する参加者をセットする
        :param member_collection:
        :return:
        """
        for member in member_collection.vil_members:
            if member.isSameHopePosition(self.position_no):
                self.members.append(member)

    def decideMembersPosition(self, conn):
        """
        このコレクションオブジェクトの参加者の役職を決定する
        :return:
        """
        for member in self.members:
            member.decidePosition(conn, self.position_no)

    def getRemainNumber(self, org_position_list: [OrganizationPosition]):
        """
        編成で決められた役職者の人数と、このコレクションオブジェクトの参加者の人数との差を返す
        :param org_position_list:
        :return:
        """
        for org_position in org_position_list:
            if org_position.isSamePositionNo(self.position_no):
                return org_position.total - len(self.members)


