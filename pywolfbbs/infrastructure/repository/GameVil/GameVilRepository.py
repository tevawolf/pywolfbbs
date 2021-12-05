from abc import ABCMeta, abstractmethod


class GameVilRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface リポジトリインターフェース
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
    def queryGameVilList(self) -> []:
        """
        GameVilのリストを返すクエリ―メソッド
        :return: GameVilのリスト
        """
        return []

    @abstractmethod
    def createGameVil(self, name: str, level: int, password: str, date: int, status: int, speech_type: int
                      , organization: int) -> int:
        """
        GameVilを永続化するメソッド
        :param name:
        :param level:
        :param password:
        :param date:
        :param status:
        :param speech_type:
        :param organization:
        :return: 村番号
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