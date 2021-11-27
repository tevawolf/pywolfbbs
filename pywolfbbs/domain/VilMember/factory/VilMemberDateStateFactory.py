from injector import Injector

from pywolfbbs.binds import VilMemberDateStateDIModule
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilSpeechNum import GameVilSpeechNum
from pywolfbbs.domain.GameVil.value.GameVilSpeechPt import GameVilSpeechPt
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.VilMember.object.VilMemberDateState import VilMemberDateState
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo


class VilMemberDateStateFactory:

    @staticmethod
    def create(vil_no: int, member_no: int, date_num: int, speech_num: int, pt: int,
               vote: int, use_ability: int) -> VilMemberDateState:

        # injector_member = Injector([VilMemberDIModule()])
        # # 投票相手の参加者情報取得
        # if vote is not None:
        #     vote_member = injector_member.get(VilMember)
        #     vote_member.setValues(GameVilNo(vil_no), PlayerId('dummy'), VilMemberNo(vote),
        #                           VilMemberName('dummy'), VilMemberTitle('dummy'), PositionNo(9999))
        #     # FIXME 要らないかも
        #     vote_member.setValuesByRepositoryMemberNo()
        # else:
        #     vote_member = None
        #
        # # 能力行使相手の参加者情報取得
        # if use_ability is not None:
        #     use_member = injector_member.get(VilMember)
        #     use_member.setValues(GameVilNo(vil_no), PlayerId('dummy'), VilMemberNo(use_ability),
        #                           VilMemberName('dummy'), VilMemberTitle('dummy'), PositionNo(9999))
        #     # FIXME 要らないかも
        #     use_member.setValuesByRepositoryMemberNo()
        # else:
        #     use_member = None

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
                                    GameVilSpeechNum(speech_num), GameVilSpeechPt(pt),
                                    # vote_member, use_member)
                                    vote_value, use_ability_value)

        return member_date_state
