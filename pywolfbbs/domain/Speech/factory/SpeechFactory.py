from datetime import datetime

from injector import Injector

from pywolfbbs.binds import SpeechDIModule
from pywolfbbs.domain.Speech.object.Speech import Speech
from pywolfbbs.domain.Speech.value.SpeechNo import SpeechNo
from pywolfbbs.domain.Player.value.PlayerName import PlayerName
from pywolfbbs.domain.Speech.value.PostDateTime import PostDateTime
from pywolfbbs.domain.Speech.value.SpeechText import SpeechText
from pywolfbbs.domain.GameVil.value.GameVliNo import GameVliNo


class SpeechFactory:

    @staticmethod
    def create(no: int, name: str, dt: datetime, title: str, text: str, thread_no: int) -> Speech:

        injector = Injector([SpeechDIModule()])
        speech = injector.get(Speech)
        speech.setValues(
            SpeechNo(no), PlayerName(name), PostDateTime(dt), SpeechText(text), GameVliNo(thread_no)
        )

        return speech
