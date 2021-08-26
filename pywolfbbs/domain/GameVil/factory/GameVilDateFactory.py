from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.object.GameVilDate import GameVilDate
from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum


class GameVilDateFactory:

    @staticmethod
    def create(num: int, status: int) -> GameVilDate:

        injector = Injector([GameVilDIModule()])
        vil = injector.get(GameVilDate)
        vil.setValues(GameVilDateNum(num), GameVilDateStatus(status))

        return vil
