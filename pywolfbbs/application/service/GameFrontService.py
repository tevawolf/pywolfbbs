from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.enum.GameVilSpeechQuantityType import GameVilSpeechQuantityType
from pywolfbbs.domain.GameVil.factory.GameVilFactory import GameVilFactory
from pywolfbbs.domain.GameVil.factory.GameVilDateFactory import GameVilDateFactory
from pywolfbbs.domain.GameVil.object.GameVilCollection import GameVilCollection
from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo


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
    def createGameVil(conn, name: str, level: str, password: str) -> None:
        """
        村作成
        :param name:
        :param level:
        :param password:
        :return:
        """
        # FIXME 仮に発言回数制と、テスト編成、5人をセット
        vil = GameVilFactory.create(9999, name, int(level), password, 0, GameVilDateStatus.プロローグ.value,
                                    GameVilSpeechQuantityType.発言回数制.value, 20, 1, 5)
        vil_no = vil.createGameVil(conn)
        vil_date = GameVilDateFactory.create(0, GameVilDateStatus.プロローグ.value)
        vil_date.createGameVilDate(conn, GameVilNo(vil_no))

        # TODO システムメッセージを作成

