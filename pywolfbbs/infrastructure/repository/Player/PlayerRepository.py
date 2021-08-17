from abc import ABCMeta, abstractmethod


class PlayerRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def addPlayer(self, playerid: str, name: str, password: bytes, tag: bytes, nonce: bytes) -> bool:
        """
        Playerを永続化するメソッド
        :param playerid:
        :param name:
        :param password:
        :return:
        """
        pass

    @abstractmethod
    def queryPlayer(self, poster_id: str) -> []:
        """
        Playerのデータを取得するクエリ―メソッド
        :param player_id:
        :return: Playerデータリスト
        """
        pass
