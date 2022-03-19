from datetime import datetime

from injector import Injector

from pywolfbbs.binds import SpeechDIModule
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.Speech.enum.SpeechType import SpeechType
from pywolfbbs.domain.Speech.object.Speech import Speech
from pywolfbbs.domain.Speech.value.SpeechNo import SpeechNo
from pywolfbbs.domain.Speech.value.PostDateTime import PostDateTime
from pywolfbbs.domain.Speech.value.SpeechText import SpeechText
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.VilMember.value.VilMemberName import VilMemberName
from pywolfbbs.domain.VilMember.value.VilMemberNo import VilMemberNo
from pywolfbbs.domain.VilMember.value.VilMemberTitle import VilMemberTitle


class SpeechFactory:

    @staticmethod
    def create(no: int, dt: datetime, type: int, text: str, player_id: str, vil_no: int, vil_date: int,
               member_no: int, member_title: str, member_name: str) -> Speech:

        injector = Injector([SpeechDIModule()])
        speech = injector.get(Speech)
        speech.setValues(
            SpeechNo(no), PostDateTime(dt), SpeechType(type), SpeechText(text), PlayerId(player_id), GameVilNo(vil_no),
            GameVilDateNum(vil_date), VilMemberNo(member_no), VilMemberTitle(member_title), VilMemberName(member_name)
        )

        return speech
