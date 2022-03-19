from injector import inject

from pywolfbbs.domain.GameVil.value.GaveVilNumberOfPeople import GameVilNumberOfPeople
from pywolfbbs.domain.Organization.factory.OrganizationPositionFactory import OrganizationPositionFactory
from pywolfbbs.domain.Organization.value.OrganizationName import OrganizationName
from pywolfbbs.domain.Organization.value.OrganizationNo import OrganizationNo
from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition
from pywolfbbs.domain.Position.value.PositionNo import PositionNo
from pywolfbbs.infrastructure.repository.Organization.OrganizationRepository import OrganizationRepository


class Organization:
    """
    @DomainObject 村の役職編成
    @EntityObject 村の編成
    @CollectionObject 村の編成に含まれる役職とその人数のセット
    """
    @inject
    def __init__(self, r: OrganizationRepository):
        self.repository = r
        self.organization_no = None   # 編成No
        self.organization_name = None  # 編成名
        self.organization_positions = None # 役職セット

    def setValues(self, no: OrganizationNo, name: OrganizationName, positions: [AbstractPosition]):
        """
        セッターメソッド
        :param no:
        :param name:
        :param positions:
        :return:
        """
        self.organization_no = no
        self.organization_name = name
        self.organization_positions = positions

    def getAllPositionOrganization(self):
        """
        全編成リストを取得
        :param member_list:
        :return:
        """
        pass

    def getHopePositionSelect(self, nop: GameVilNumberOfPeople) -> []:
        """
        役職希望選択リストを取得
        :param nop: 参加人数
        :return:
        """
        return self.repository.queryOrganizationPositionNameList(self.organization_no.getValue(), nop.getValue())

    def setOrganizationPositionsByRepository(self, nop: GameVilNumberOfPeople) -> []:
        """
        役職ごとの定員リストを取得
        :param nop: 参加人数
        :return:
        """
        results = self.repository.queryOrganizationPositionTotalList(self.organization_no.getValue(), nop.getValue())
        for result in results:
            organization_position = OrganizationPositionFactory.create(
                self.organization_no.getValue(), nop.getValue(), int(result[0]), int(result[1]))
            self.organization_positions.append(organization_position)
