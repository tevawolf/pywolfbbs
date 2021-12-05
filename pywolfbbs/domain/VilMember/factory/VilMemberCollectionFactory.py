from injector import Injector

from pywolfbbs.binds import VilMemberDIModule
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.VilMember.object.VilMemberCollection import VilMemberCollection


class VilMemberCollectionFactory:

    @staticmethod
    def create(vil_no: int) -> VilMemberCollection:

        injector = Injector([VilMemberDIModule()])
        vilmembers = injector.get(VilMemberCollection)
        vilmembers.setValues(GameVilNo(vil_no))

        return vilmembers
