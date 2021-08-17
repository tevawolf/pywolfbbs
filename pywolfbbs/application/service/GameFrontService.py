from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.factory.GameVliFactory import GameVliFactory
from pywolfbbs.domain.GameVil.object.GameFront import GameFront


class GameFrontService:
    """
    初期起動表示
    村作成
    """

    @staticmethod
    def initDisplay() -> GameFront:
        injector = Injector([GameVilDIModule()])
        front = injector.get(GameFront)
        return front

    @staticmethod
    def createGameVil(name: str, level: str, password: str) -> None:
        vil = GameVliFactory.create(9999, name, int(level), password)
        vil.createGameVil()
