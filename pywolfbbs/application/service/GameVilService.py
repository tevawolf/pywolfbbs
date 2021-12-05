from pywolfbbs.domain.GameVil.factory.GameVilDateCollectionFactory import GameVilDateCollectionFactory
from pywolfbbs.domain.GameVil.object.GameVilDateCollection import GameVilDateCollection
from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.factory.GameVilFactory import GameVilFactory
from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.domain.GameVil.enum.GameVilPublicLevel import GameVilPublicLevel


class GameVilService:
    """
    村のサービスオブジェクト
    """

    @staticmethod
    def getVilDate(no: int) -> (GameVil, GameVilDateCollection, ):
        """
        村番号に該当する村情報を取得
        :param no:
        :param disp_date:
        :return:
        """
        # 公開レベル、現在日、現在日ステータスもダミー
        vil = GameVilFactory.create(no, 'dummy', GameVilPublicLevel.公開.value, 'dummy', 0, GameVilDateStatus.プロローグ.value, 0, 0)
        vil.setValuesByRepository()

        dates = GameVilDateCollectionFactory.create(no)

        return vil, dates

    @staticmethod
    def authenticatePassword(no: int, password: str) -> bool:
        """
        パスワード認証
        :param no:
        :param password:
        :return:
        """
        # 公開レベル、現在日、現在日ステータスもダミー
        vil = GameVilFactory.create(no, 'dummy', GameVilPublicLevel.公開.value, password, 0, GameVilDateStatus.プロローグ.value, 0, 0)
        return vil.isPasswordMatched()
