from abc import ABCMeta, abstractmethod


class VilMemberDateStateRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def queryVilMemberDateState(self, vil_no: int, member_no: int, date: int):
        """
        vil_no、member_no、date_numに一致するVilMemberDateStateを返すクエリ―メソッド
        （特定の参加者の、現在日の状態を取得）
        :param vil_no:
        :param member_no:
        :param date:
        :return:
        """
        pass

    @abstractmethod
    def queryVilMemberDateStateList(self, vil_no: int, member_no: int):
        """
        vil_no、member_noに一致するVilMemberDateStateを返すクエリ―メソッド
        （特定の参加者の全日付の状態を取得）
        :param vil_no:
        :param member_no:
        :return:
        """
        pass

    @abstractmethod
    def queryVilMemberDateStateDateList(self, vil_no: int, date: int):
        """
        vil_no、dateに一致するVilMemberDateStateを返すクエリ―メソッド
        （特定の日付の全参加者の状態を取得）
        :param vil_no:
        :param date:
        :return:
        """
        pass

    @abstractmethod
    def addMemberDateState(self, vil_no: int, member_no: int, date: int, speech_num: int, pt: int, vote: int, use: int):
        """
        VilMemberDateStateを永続化するメソッド
        :param vil_no:　村番号
        :param member_no:　参加者番号
        :param date:
        :param speech_num:
        :param pt:
        :param vote:
        :param use:

        :return: 追加の成否
        """
        pass
