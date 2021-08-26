from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.factory.GameVliFactory import GameVliFactory
from pywolfbbs.domain.GameVil.factory.GameVilDateFactory import GameVilDateFactory
from pywolfbbs.domain.GameVil.object.GameFront import GameFront
from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus


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
        # 現在日ステータスはダミー
        vil = GameVliFactory.create(9999, name, int(level), password, 0, GameVilDateStatus.プロローグ)
        vil_no = vil.createGameVil()
        vil_date = GameVilDateFactory.create(0, GameVilDateStatus.プロローグ)
        vil_date.createGameVilDate(vil_no)
