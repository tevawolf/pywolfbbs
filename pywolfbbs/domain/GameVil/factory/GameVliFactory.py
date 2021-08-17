from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.domain.GameVil.value.GameVliName import GameVliName
from pywolfbbs.domain.GameVil.value.GameVliNo import GameVliNo
from pywolfbbs.domain.GameVil.value.GameVliPassword import GameVliPassword


class GameVliFactory:

    @staticmethod
    def create(no: int, name: str, level: int, password: str) -> GameVil:

        injector = Injector([GameVilDIModule()])
        vil = injector.get(GameVil)
        vil.setValues(GameVliNo(no), GameVliName(name), GameVilPublicLevel(level), GameVliPassword(password))

        return vil
