from injector import Injector

from pywolfbbs.binds import OrganizationDIModule
from pywolfbbs.domain.Organization.object.Organization import Organization
from pywolfbbs.domain.Organization.value.OrganizationName import OrganizationName
from pywolfbbs.domain.Organization.value.OrganizationNo import OrganizationNo
from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition


class OrganizationFactory:

    @staticmethod
    def create(no: int, name: str, position_list: [AbstractPosition]) -> Organization:

        injector = Injector([OrganizationDIModule()])
        organization = injector.get(Organization)
        organization.setValues(OrganizationNo(no), OrganizationName(name), position_list)

        return organization

    @staticmethod
    def create_only_no(no: int):
        injector = Injector([OrganizationDIModule()])
        organization = injector.get(Organization)
        organization.setValues(OrganizationNo(no), OrganizationName('dummy'), [])

        return organization

