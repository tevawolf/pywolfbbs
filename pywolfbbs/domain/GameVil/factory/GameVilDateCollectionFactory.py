from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.object.GameVilDateCollection import GameVilDateCollection
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo


class GameVilDateCollectionFactory:

    @staticmethod
    def create(vil_no: int) -> GameVilDateCollection:

        injector = Injector([GameVilDIModule()])
        dates = injector.get(GameVilDateCollection)
        dates.setValues(GameVilNo(vil_no))
        dates.setVilDateList()

        return dates
