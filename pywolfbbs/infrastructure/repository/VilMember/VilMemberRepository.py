from abc import ABCMeta, abstractmethod


class VilMemberRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def queryVilMember(self, vil_no: int, player_id: str):
        """
        vil_no、player_idに一致するVilMemberを返すクエリ―メソッド
        :param vil_no:
        :param player_id:
        :return:
        """
        pass

    @abstractmethod
    def addMember(self, vil_no: int, player_id: str, member_name: str, member_title: str):
        """
        VilMemberを永続化するメソッド
        :param vil_no:　村番号
        :param player_id:　プレイヤーID
        :param member_name:　参加キャラクター名
        :param member_title:　参加キャラクター肩書き
        :return: 追加の成否
        """
        pass
