from injector import Injector

from pywolfbbs.binds import OrganizationDIModule
from pywolfbbs.domain.Organization.object.Organization import Organization
from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition


class OrganizationFactory:

    @staticmethod
    def create(no: int, name: str, position_list: [AbstractPosition]) -> Organization:

        injector = Injector([OrganizationDIModule()])
        organization = injector.get(Organization)
        organization.setValues(no, name, position_list)

        return organization
