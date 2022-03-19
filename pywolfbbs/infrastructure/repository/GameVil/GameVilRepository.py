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
    def createGameVil(self, conn, name: str, level: int, password: str, date: int, status: int, speech_type: int
                      , max_speech: int, organization: int, number_of_people: int) -> int:
        """
        GameVilを永続化するメソッド
        :param name:
        :param level:
        :param password:
        :param date:
        :param status:
        :param speech_type:
        :param max_speech:
        :param organization:
        :param number_of_people:
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

    @abstractmethod
    def updateCurrentDate(self, conn, no: int, date: int, status: int) -> bool:
        """
        GameVilのcurrent_date, current_date_statusを更新するメソッド
        :param no:
        :param date:
        :param status
        :return:
        """
        pass
