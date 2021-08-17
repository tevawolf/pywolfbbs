from abc import ABCMeta, abstractmethod


class GameFrontRepository(metaclass=ABCMeta):
    """
    @RepositotyInterface リポジトリインターフェース
    """

    @abstractmethod
    def queryGameVilList(self) -> []:
        """
        GameVilのリストを返すクエリ―メソッド
        :return: GameVilのリスト
        """
        return []
