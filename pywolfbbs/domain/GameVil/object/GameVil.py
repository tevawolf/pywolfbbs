from injector import inject

from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.enum.GameVilSpeechQuantityType import GameVilSpeechQuantityType
from pywolfbbs.domain.GameVil.value.AbstractGameVilSpeechQuantity import AbstractGameVilSpeechQuantity
from pywolfbbs.domain.GameVil.value.GameVilSpeechNum import GameVilSpeechNum
from pywolfbbs.domain.GameVil.value.GameVilSpeechPt import GameVilSpeechPt
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.GameVil.enum.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.domain.GameVil.value.GameVilName import GameVilName
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilPassword import GameVilPassword
from pywolfbbs.domain.GameVil.value.GaveVilNumberOfPeople import GameVilNumberOfPeople
from pywolfbbs.domain.Organization.value.OrganizationNo import OrganizationNo
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
        self.speech_quantity_type = None
        self.max_speech_quantity = None
        self.organization_no = None
        self.number_of_people = None

    def setValues(self, no: GameVilNo, name: GameVilName, level: GameVilPublicLevel, password: GameVilPassword,
                  date: GameVilDateNum, status: GameVilDateStatus, s_q_type: GameVilSpeechQuantityType,
                  max_speech: AbstractGameVilSpeechQuantity, organization: OrganizationNo, number_of_people: GameVilNumberOfPeople) -> None:
        """
        セッターメソッド
        :param no:　村No.
        :param name:　村名
        :param level:　公開レベル
        :param password: 入村・閲覧パスワード
        :param date: 現在日
        :param status: 現在日の状態（プロローグ／進行中／エピローグなど）
        :param s_q_type: 発言数量タイプ
        :param max_speech: 最大発言数量
        :param organization: 編成No
        :param number_of_people: 村の人数
        :return: なし
        """
        self.vil_no = no
        self.vil_name = name
        self.public_level = level
        self.password = password
        self.current_date = date
        self.current_date_status = status
        self.speech_quantity_type = s_q_type
        self.max_speech_quantity = max_speech
        self.organization_no = organization
        self.number_of_people = number_of_people

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
        self.speech_quantity_type = GameVilSpeechQuantityType(vil[4])
        if self.speech_quantity_type == GameVilSpeechQuantityType.発言回数制:
            self.max_speech_quantity = GameVilSpeechNum(vil[5])
        elif self.speech_quantity_type == GameVilSpeechQuantityType.発言pt制:
            self.max_speech_quantity = GameVilSpeechPt(vil[5])
        self.organization_no = OrganizationNo(vil[6])
        self.number_of_people = GameVilNumberOfPeople(vil[7])

    def createGameVil(self, conn) -> int:
        """
        村を作成
        :return: 村番号
        """
        # 永続化
        return self.repository.createGameVil(conn,
            self.vil_name.getValue(),
            self.public_level.value,
            self.password.getValue(),
            self.current_date.getValue(),
            self.current_date_status.value,
            self.speech_quantity_type.value,
            self.max_speech_quantity.getValue(),
            self.organization_no.getValue(),
            self.number_of_people.getValue(),
        )

    def isPasswordMatched(self) -> bool:
        """
        村に設定されたパスワードと入力値が一致するか判定
        :param password:　パスワード
        :return:　判定結果
        """
        db_password = self.repository.queryGameVilPassword(self.vil_no.getValue())
        return self.password.getValue() == db_password

    def nextDate(self, conn, next_date_status) -> GameVilDateNum:
        """
        村の現在日を1進め、ステータスを更新する。
        :return:
        """
        next_date = self.current_date.nextDate()

        self.repository.updateCurrentDate(conn, self.vil_no.getValue(), next_date.getValue(), next_date_status.value)

        return next_date
        # return
