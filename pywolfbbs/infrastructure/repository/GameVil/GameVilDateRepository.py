from abc import ABCMeta, abstractmethod


class GameVilDateRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface リポジトリインターフェース
    """
    @abstractmethod
    def queryGameVilDateList(self, vil_no: int) -> []:
        """
        vil_noに一致するGameVilDateのリストを返すクエリーメソッド
        :param vil_no: 村No
        :return: GameVilDateのリスト
        """
        return []

    @abstractmethod
    def createGameVilDate(self, date: int, vil_no: int, status: int) -> bool:
        """
        GameVilDateを永続化するメソッド
        :return:
        """
        pass
