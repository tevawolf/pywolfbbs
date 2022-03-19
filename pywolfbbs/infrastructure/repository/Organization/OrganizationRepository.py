from abc import ABCMeta, abstractmethod


class OrganizationRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface リポジトリインターフェース
    """
    @abstractmethod
    def queryOrganizationPositionTotalList(self, organization_no: int, nop: int) -> []:
        """
        編成が持つ役職と定員のリスト（ダミーを除く）を取得するクエリーメソッド
        :param organization_no: 編成No
        :param nop: 参加者の人数
        :return: 編成役職リスト
        """
        pass

    @abstractmethod
    def queryOrganizationPositionNameList(self, organization_no: int, nop: int) -> []:
        """
        編成が持つ役職と名前のリスト（ダミーを除く）を取得するクエリーメソッド
        :param organization_no: 編成No
        :param nop: 参加者の人数
        :return: 編成役職リスト
        """
        pass
