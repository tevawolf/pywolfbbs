from injector import Injector

from pywolfbbs.binds import SpeechDIModule
from pywolfbbs.domain.Speech.object.SpeechCollection import SpeechCollection
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo


class SpeechCollectionFactory:

    @staticmethod
    def create(vil_no: int) -> SpeechCollection:

        injector = Injector([SpeechDIModule()])
        speeches = injector.get(SpeechCollection)
        speeches.setValues(GameVilNo(vil_no))

        return speeches
