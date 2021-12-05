from injector import Injector

from pywolfbbs.binds import VilMemberDateStateDIModule
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilSpeechNum import GameVilSpeechNum
from pywolfbbs.domain.GameVil.value.GameVilSpeechPt import GameVilSpeechPt
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.VilMember.enum.VilMemberPlaces import VilMemberPlaces
from pywolfbbs.domain.VilMember.object.VilMemberDateState import VilMemberDateState
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo


class VilMemberDateStateFactory:

    @staticmethod
    def create(vil_no: int, member_no: int, date_num: int, place: int, speech_num: int, pt: int,
               vote: int, use_ability: int) -> VilMemberDateState:

        injector_member_date_state = Injector([VilMemberDateStateDIModule()])
        member_date_state = injector_member_date_state.get(VilMemberDateState)

        if vote is not None:
            vote_value = VilMemberNo(vote)
        else:
            vote_value = None

        if use_ability is not None:
            use_ability_value = VilMemberNo(use_ability)
        else:
            use_ability_value = None

        member_date_state.setValues(GameVilNo(vil_no), VilMemberNo(member_no), GameVilDateNum(date_num),
                                    VilMemberPlaces(place), GameVilSpeechNum(speech_num), GameVilSpeechPt(pt),
                                    vote_value, use_ability_value)

        return member_date_state
