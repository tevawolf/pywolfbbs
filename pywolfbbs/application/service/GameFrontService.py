from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.factory.GameVilFactory import GameVilFactory
from pywolfbbs.domain.GameVil.factory.GameVilDateFactory import GameVilDateFactory
from pywolfbbs.domain.GameVil.object.GameVilCollection import GameVilCollection
from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus


class GameFrontService:
    """
    フロントページのサービスオブジェクト
    """

    @staticmethod
    def initDisplay() -> GameVilCollection:
        """
        初期起動表示
        :return:
        """
        injector = Injector([GameVilDIModule()])
        front = injector.get(GameVilCollection)
        return front

    @staticmethod
    def createGameVil(name: str, level: str, password: str) -> None:
        """
        村作成
        :param name:
        :param level:
        :param password:
        :return:
        """
        # 現在日ステータスはダミー
        vil = GameVilFactory.create(9999, name, int(level), password, 0, GameVilDateStatus.プロローグ)
        vil_no = vil.createGameVil()
        vil_date = GameVilDateFactory.create(0, GameVilDateStatus.プロローグ)
        vil_date.createGameVilDate(vil_no)

