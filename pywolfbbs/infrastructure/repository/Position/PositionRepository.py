from abc import ABCMeta, abstractmethod


class PositionRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def queryPositionById(self, position_no: int) -> []:
        """
        position_noに一致するPositionを返すクエリ―メソッド
        :param position_no:
        :return:
        """
        pass