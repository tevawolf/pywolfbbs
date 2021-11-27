from injector import Injector

from pywolfbbs.binds import VilMemberDIModule
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.Position.value.PositionNo import PositionNo
from pywolfbbs.domain.VilMember.object.VilMember import VilMember
from pywolfbbs.domain.VilMember.value.VilMemberName import VilMemberName
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo
from pywolfbbs.domain.VilMember.value.VilMemberTitle import VilMemberTitle


class VilMemberFactory:

    @staticmethod
    def create(vil_no: int, player_id: str, member_no: int, name: str, title: str, hope_position: int, position: int) -> VilMember:

        injector = Injector([VilMemberDIModule()])
        member = injector.get(VilMember)
        member.setValues(GameVilNo(vil_no), PlayerId(player_id), VilMemberNo(member_no), VilMemberName(name),
                         VilMemberTitle(title), PositionNo(hope_position), PositionNo(position))

        return member
