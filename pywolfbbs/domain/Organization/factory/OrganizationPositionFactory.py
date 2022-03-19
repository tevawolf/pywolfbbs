from injector import Injector

from pywolfbbs.binds import OrganizationDIModule, OrganizationPositionDIModule
from pywolfbbs.domain.GameVil.value.GaveVilNumberOfPeople import GameVilNumberOfPeople
from pywolfbbs.domain.Organization.object.OrganizationPosition import OrganizationPosition
from pywolfbbs.domain.Organization.value.OrganizationNo import OrganizationNo
from pywolfbbs.domain.Organization.value.OrganizationPositionTotalNumber import OrganizationPositionTotalNumber
from pywolfbbs.domain.Position.value.PositionNo import PositionNo


class OrganizationPositionFactory:

    @staticmethod
    def create(no: int, nop: int, position_no: int, total: int) -> OrganizationPosition:

        injector = Injector([OrganizationPositionDIModule()])
        organization_position = injector.get(OrganizationPosition)
        organization_position.setValues(PositionNo(position_no), GameVilNumberOfPeople(nop),
                                        OrganizationPositionTotalNumber(total))

        return organization_position

    @staticmethod
    def create_only_pk(no: int, nop: int, position_no: int) -> OrganizationPosition:
        injector = Injector([OrganizationPositionDIModule()])
        organization_position = injector.get(OrganizationPosition)
        organization_position.setValues(OrganizationNo(no), GameVilNumberOfPeople(nop), PositionNo(position_no), 0)

        return organization_position
