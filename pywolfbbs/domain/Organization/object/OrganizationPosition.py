from injector import inject

from pywolfbbs.domain.GameVil.value.GaveVilNumberOfPeople import GameVilNumberOfPeople
from pywolfbbs.domain.Organization.value.OrganizationPositionTotalNumber import OrganizationPositionTotalNumber
from pywolfbbs.domain.Position.value.PositionNo import PositionNo
from pywolfbbs.infrastructure.repository.Organization.OrganizationPositionRepository import \
    OrganizationPositionRepository


class OrganizationPosition:
    """
    @DomainObject 編成に含まれる役職
    @EntityObject 村の編成に含まれる役職とその人数
    """
    @inject
    def __init__(self, r: OrganizationPositionRepository):
        self.repository = r
        self.position_no = None     # 役職No
        self.number_of_people = None    # 参加人数
        self.total = None       # 総数

    def setValues(self, position_no: PositionNo, number_of_people: GameVilNumberOfPeople, total: OrganizationPositionTotalNumber):
        self.position_no = position_no
        self.number_of_people = number_of_people
        self.total = total

    def isOverHopeNumber(self, hope_number: GameVilNumberOfPeople) -> bool:
        """
        渡された役職希望者の人数が、編成で決められた役職者の人数を超えているか判定
        :param hope_number:
        :return:
        """
        return hope_number.getValue() > self.number_of_people.getValue()

    def isSamePositionNo(self, position_no: PositionNo):
        """
        渡された役職Noがこのオブジェクトの役職Noと同じか判定
        :param position_no:
        :return:
        """
        return self.position_no.equalNumber(position_no)