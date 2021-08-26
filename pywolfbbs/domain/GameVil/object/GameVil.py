import copy

from injector import inject

from pywolfbbs.domain.GameVil.factory.GameVilDateFactory import GameVilDateFactory
from pywolfbbs.domain.GameVil.object.GameVilDate import GameVilDate
from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.Speech.factory.SpeechFactory import SpeechFactory
from pywolfbbs.domain.Speech.object.Speech import Speech
from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.domain.GameVil.value.GameVilName import GameVilName
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilPassword import GameVilPassword
from pywolfbbs.infrastructure.repository.GameVil.GameVilRepository import GameVilRepository


class GameVil:
    """
    @DomainObject 村
    @EntityObject （一意性のある）村を表す
    @CollectionObject 発言のコレクション FIXME 単独でコレクションオブジェクトをつくり、それをこのクラスに持たせるべきか？
    """
    @inject
    def __init__(self, r: GameVilRepository):
        self.repository = r
        self.vil_no = None
        self.vil_name = None
        self.public_level = None
        self.password = None
        self.dates = []
        self.current_date = None
        self.current_date_status = None
        self.speechs = []

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

    def setVilDateList(self):
        """
        リポジトリから村の日付のリストを取得し、保持する
        :return: なし
        """
        date_list = self.repository.queryVilDateList(self.vil_no.getValue())
        for s in date_list:
            date = GameVilDateFactory.create(s[0], s[2])
            self.dates.append(date)

    def setSpeechList(self, disp_date: int):
        """
        リポジトリから発言のリストを取得し、保持する
        :return: なし
        """
        speech_list = self.repository.querySpeechList(self.vil_no.getValue(), disp_date)
        for s in speech_list:
            speech = SpeechFactory.create(s[0], s[1], s[2], s[3], s[4], s[5])
            self.speechs.append(speech)

    def postAllDates(self) -> [GameVilDate]:
        """
        村の日付をすべて提示する
        :return　村の日付リストのコピー
        """
        return copy.deepcopy(self.dates)

    def postAllSpeechs(self) -> [Speech]:
        """
        発言をすべて提示する
        :return　発言リストのコピー
        """
        return copy.deepcopy(self.speechs)

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
