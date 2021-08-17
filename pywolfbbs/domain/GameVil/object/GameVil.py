import copy

from injector import inject

from pywolfbbs.domain.Speech.factory.SpeechFactory import SpeechFactory
from pywolfbbs.domain.Speech.object.Speech import Speech
from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.domain.GameVil.value.GameVliName import GameVliName
from pywolfbbs.domain.GameVil.value.GameVliNo import GameVliNo
from pywolfbbs.domain.GameVil.value.GameVliPassword import GameVliPassword
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
        self.speechs = []

    def setValues(self, no: GameVliNo, name: GameVliName, level: GameVilPublicLevel, password: GameVliPassword) -> None:
        """
        セッターメソッド
        :param no:　村No.
        :param name:　村名
        :param level:　公開レベル
        :param password: 入村・閲覧パスワード
        :return: なし
        """
        self.vil_no = no
        self.vil_name = name
        self.public_level = level
        self.password = password

    def setValuesByRepository(self) -> None:
        """
        DB取得値をセット
        :return: なし
        """
        vil = self.repository.queryGameVil(self.vil_no.getValue())
        self.vil_name = GameVliName(vil[0])
        self.public_level = GameVilPublicLevel(int(vil[1]))

    def setSpeechList(self):
        """
        リポジトリから発言のリストを取得し、保持する
        :return: なし
        """
        speech_list = self.repository.querySpeechList(self.vil_no.getValue())
        for s in speech_list:
            speech = SpeechFactory.create(s[0], s[1], s[2], s[3], s[4], s[5])
            self.speechs.append(speech)

    def postAllSpeechs(self) -> [Speech]:
        """
        発言をすべて提示する
        :return　発言リストのコピー
        """
        return copy.deepcopy(self.speechs)

    def createGameVil(self) -> None:
        """
        村を作成
        :return: なし
        """
        # 永続化
        self.repository.createGameVil(
            self.vil_name.getValue(),
            self.public_level.value,
            self.password.getValue()
        )

    def isPasswordMatched(self) -> bool:
        """
        村に設定されたパスワードと入力値が一致するか判定
        :param password:　パスワード
        :return:　判定結果
        """
        db_password = self.repository.queryGameVilPassword(self.vil_no.getValue())
        return self.password.getValue() == db_password
