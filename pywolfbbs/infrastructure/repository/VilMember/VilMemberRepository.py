from abc import ABCMeta, abstractmethod


class VilMemberRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def queryVilMemberByPlayerId(self, vil_no: int, player_id: str) -> []:
        """
        vil_no、player_idに一致するVilMemberを返すクエリ―メソッド
        :param vil_no:
        :param player_id:
        :return:
        """
        pass

    @abstractmethod
    def queryVilMemberByMemberNo(self, vil_no: int, member_no: int) -> []:
        """
        vil_no、member_noに一致するVilMemberを返すクエリ―メソッド
        :param vil_no:
        :param member_no:
        :return:
        """
        pass

    @abstractmethod
    def queryVilMemberList(self, vil_no: int) -> []:
        """
        vil_noに一致するVilMemberのリストを返すクエリ―メソッド
        :param vil_no:
        :return:
        """
        pass

    @abstractmethod
    def addMember(self, conn, vil_no: int, player_id: str, member_name: str, member_title: str) -> int:
        """
        VilMemberを永続化するメソッド
        :param vil_no:　村番号
        :param player_id:　プレイヤーID
        :param member_name:　参加キャラクター名
        :param member_title:　参加キャラクター肩書き
        :return: 参加者No
        """
        pass

    @abstractmethod
    def setHopePosition(self, conn, vil_no: int, player_id: str, position_no: int) -> bool:
        """
        hope_positionをUpdateするメソッド
        :param vil_no:　村番号
        :param player_id:　プレイヤーID
        :param position_no: 希望役職No
        :return:
        """
        pass

    @abstractmethod
    def setPosition(self, conn, vil_no: int, player_id: str, position_no: int) -> bool:
        """
        positionをUpdateするメソッド
        :param vil_no:　村番号
        :param player_id:　プレイヤーID
        :param position_no: 役職No
        :return:
        """
        pass
