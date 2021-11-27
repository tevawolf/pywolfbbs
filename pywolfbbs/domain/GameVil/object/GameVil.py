from injector import inject

from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.GameVil.enum.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.domain.GameVil.value.GameVilName import GameVilName
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilPassword import GameVilPassword
from pywolfbbs.infrastructure.repository.GameVil.GameVilRepository import GameVilRepository


class GameVil:
    """
    @DomainObject 村
    @EntityObject （一意性のある）村を表す
    """
    @inject
    def __init__(self, r: GameVilRepository):
        self.repository = r
        self.vil_no = None
        self.vil_name = None
        self.public_level = None
        self.password = None
        self.current_date = None
        self.current_date_status = None
        self.organization_no = None

    def setValues(self, no: GameVilNo, name: GameVilName, level: GameVilPublicLevel, password: GameVilPassword,
                  date: GameVilDateNum, status: GameVilDateStatus) -> None:
        """
        セッターメソッド
        :param no:　村No.
        :param name:　村名
        :param level:　公開レベル
        :param password: 入村・閲覧パスワード
        :param date: 現在日
        :param status: 現在日の状態（プロローグ／進行中／エピローグなど）
        :return: なし
        """
        self.vil_no = no
        self.vil_name = name
        self.public_level = level
        self.password = password
        self.current_date = date
        self.current_date_status = status

    def setValuesByRepository(self) -> None:
        """
        DB取得値をセット
        :return: なし
        """
        vil = self.repository.queryGameVil(self.vil_no.getValue())
        self.vil_name = GameVilName(vil[0])
        self.public_level = GameVilPublicLevel(int(vil[1]))
        self.current_date = GameVilDateNum(int(vil[2]))
        self.current_date_status = GameVilDateStatus(int(vil[3]))

    def createGameVil(self) -> int:
        """
        村を作成
        :return: 村番号
        """
        # 永続化
        return self.repository.createGameVil(
            self.vil_name.getValue(),
            self.public_level.value,
            self.password.getValue(),
            self.current_date.getValue(),
            self.current_date_status.value
        )

    def isPasswordMatched(self) -> bool:
        """
        村に設定されたパスワードと入力値が一致するか判定
        :param password:　パスワード
        :return:　判定結果
        """
        db_password = self.repository.queryGameVilPassword(self.vil_no.getValue())
        return self.password.getValue() == db_password
