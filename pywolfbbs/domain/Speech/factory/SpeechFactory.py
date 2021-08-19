from datetime import datetime

from injector import Injector

from pywolfbbs.binds import SpeechDIModule
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.Speech.object.Speech import Speech
from pywolfbbs.domain.Speech.value.SpeechNo import SpeechNo
from pywolfbbs.domain.Speech.value.PostDateTime import PostDateTime
from pywolfbbs.domain.Speech.value.SpeechText import SpeechText
from pywolfbbs.domain.GameVil.value.GameVliNo import GameVliNo


class SpeechFactory:

    @staticmethod
    def create(no: int, dt: datetime, text: str, player_id: str, vil_no: int) -> Speech:

        injector = Injector([SpeechDIModule()])
        speech = injector.get(Speech)
        speech.setValues(
            SpeechNo(no), PostDateTime(dt), SpeechText(text), PlayerId(player_id), GameVliNo(vil_no)
        )

        return speech
