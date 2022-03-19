from injector import inject

from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.infrastructure.repository.GameVil.GameVilDateRepository import GameVilDateRepository


class GameVilDate:
    """
    @DomainObject 村日にち
    @EntityObject （一意性のある）村の日にちを表す
    """
    @inject
    def __init__(self, r: GameVilDateRepository):
        self.repository = r
        self.date_num = None
        self.date_status = None

    def setValues(self, num: GameVilDateNum, status: GameVilDateStatus) -> None:
        """
        セッターメソッド
        :param num:
        :param status:
        :return:
        """
        self.date_num = num
        self.date_status = status

    def createGameVilDate(self, conn, vil_no: GameVilNo) -> None:
        """
        村の日にちを作成
        :return: なし
        """
        # 永続化
        self.repository.createGameVilDate(conn,
            self.date_num.getValue(),
            vil_no.getValue(),
            self.date_status.value
        )



