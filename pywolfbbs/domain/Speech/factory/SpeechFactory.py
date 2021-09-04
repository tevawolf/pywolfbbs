from datetime import datetime

from injector import Injector

from pywolfbbs.binds import SpeechDIModule
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.Speech.object.Speech import Speech
from pywolfbbs.domain.Speech.value.SpeechNo import SpeechNo
from pywolfbbs.domain.Speech.value.PostDateTime import PostDateTime
from pywolfbbs.domain.Speech.value.SpeechText import SpeechText
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo


class SpeechFactory:

    @staticmethod
    def create(no: int, dt: datetime, text: str, player_id: str, vil_no: int, vil_date: int) -> Speech:

        injector = Injector([SpeechDIModule()])
        speech = injector.get(Speech)
        speech.setValues(
            SpeechNo(no), PostDateTime(dt), SpeechText(text), PlayerId(player_id), GameVilNo(vil_no),
            GameVilDateNum(vil_date)
        )

        return speech
