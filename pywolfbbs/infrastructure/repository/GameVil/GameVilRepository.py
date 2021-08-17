from abc import ABCMeta, abstractmethod


class GameVilRepository(metaclass=ABCMeta):
    """
    @RepositotyInterface リポジトリインターフェース
    """
    @abstractmethod
    def queryGameVil(self, no: int) -> []:
        """
        noに一致するGameVilを返すクエリ―メソッド
        :param no: 村No
        :return: Thread
        """
        pass

    @abstractmethod
    def querySpeechList(self, no: int) -> []:
        """
        Speechのリストを返すクエリーメソッド
        :return: Speechのリスト
        """
        return []

    @abstractmethod
    def createGameVil(self, name: str, level: int, password: str) -> bool:
        """
        GameVilを永続化するメソッド
        :param name:
        :return:
        """
        pass

    @abstractmethod
    def queryGameVilPassword(self, no: int) -> str:
        """
        GameVilに設定されたパスワードを返すクエリーメソッド
        :param no:
        :param password:
        :return:
        """
        pass