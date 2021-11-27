from injector import Injector

from pywolfbbs.binds import VilMemberDateStateDIModule
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.VilMember.object.VilMemberDateStateCollection import VilMemberDateStateCollection
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo


class VilMemberDateStateCollectionFactory:

    @staticmethod
    def create(vil_no: int, member_no: int, date_num: int) -> VilMemberDateStateCollection:

        injector = Injector([VilMemberDateStateDIModule()])
        vilmembers_state = injector.get(VilMemberDateStateCollection)
        vilmembers_state.setValues(GameVilNo(vil_no), VilMemberNo(member_no), GameVilDateNum(date_num))

        return vilmembers_state
