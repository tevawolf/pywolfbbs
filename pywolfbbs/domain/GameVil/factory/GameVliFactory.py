from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.domain.GameVil.value.GameVilName import GameVilName
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilPassword import GameVilPassword
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum


class GameVliFactory:

    @staticmethod
    def create(no: int, name: str, level: int, password: str, date: int, status: int) -> GameVil:

        injector = Injector([GameVilDIModule()])
        vil = injector.get(GameVil)
        vil.setValues(GameVilNo(no), GameVilName(name), GameVilPublicLevel(level), GameVilPassword(password),
                      GameVilDateNum(date), GameVilDateStatus(status))

        return vil
