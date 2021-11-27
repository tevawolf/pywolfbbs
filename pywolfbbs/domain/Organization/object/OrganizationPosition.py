from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition
from pywolfbbs.domain.Organization.value.OrganizationPositionNumber import OrganizationPositionNumber
from pywolfbbs.infrastructure.repository.Organization.OrganizationRepository import OrganizationRepository


class OrganizationPosition:
    """
    @DomainObject 編成に含まれる役職
    @EntityObject 村の編成に含まれる役職とその人数
    """
    def __init__(self, r: OrganizationRepository):
        self.repository = r
        self.position = None     # 役職
        self.total = None       # 総数

    def setValues(self, position: AbstractPosition, total: OrganizationPositionNumber):
        self.position = position
        self.total = total
