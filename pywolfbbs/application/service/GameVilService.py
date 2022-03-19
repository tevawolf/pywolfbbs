from pywolfbbs.domain.GameVil.factory.GameVilDateCollectionFactory import GameVilDateCollectionFactory
from pywolfbbs.domain.GameVil.object.GameVilDateCollection import GameVilDateCollection
from pywolfbbs.domain.GameVil.factory.GameVilFactory import GameVilFactory
from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.domain.GameVil.value.GameVilPassword import GameVilPassword


class GameVilService:
    """
    村のサービスオブジェクト
    """

    @staticmethod
    def getVilDate(no: int) -> (GameVil, GameVilDateCollection, ):
        """
        村番号に該当する村情報・村の日付情報を取得
        :param no:
        :param disp_date:
        :return:
        """

        vil = GameVilFactory.create_only_no(no)
        vil.setValuesByRepository()

        dates = GameVilDateCollectionFactory.create(no)

        return vil, dates

    @staticmethod
    def getVil(no: int) -> GameVil:
        """
        村番号に該当する村情報を取得
        :param no:
        :return:
        """

        vil = GameVilFactory.create_only_no(no)
        vil.setValuesByRepository()

        return vil

    @staticmethod
    def authenticatePassword(no: int, password: str) -> bool:
        """
        パスワード認証
        :param no:
        :param password:
        :return:
        """
        vil = GameVilFactory.create_only_no(no)
        vil.password = GameVilPassword(password)

        return vil.isPasswordMatched()
