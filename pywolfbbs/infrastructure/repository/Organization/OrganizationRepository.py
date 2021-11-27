from abc import ABCMeta, abstractmethod


class OrganizationRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface リポジトリインターフェース
    """
    @abstractmethod
    def queryOrganizationPositionList(self, organization_no: int, nop: int) -> []:
        """
        編成が持つ役職のリスト（ダミーを除く）を取得するクエリーメソッド
        :param organization_no: 編成No
        :param nop: 参加者の人数
        :return: 編成役職リスト
        """
        pass
