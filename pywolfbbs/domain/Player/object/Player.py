from typing import Union

from Crypto.Cipher import AES
from injector import inject

from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.Player.value.PlayerName import PlayerName
from pywolfbbs.domain.Player.value.PlayerPassword import PlayerPassword
from pywolfbbs.infrastructure.repository.Player.PlayerRepository import PlayerRepository


class Player:
    """
    @DomainObject プレイヤー（PL）
    @EntityObject （一意性のある）プレイヤーを表す
    """

    KEY = b'tevawolf20210701'

    @inject
    def __init__(self, r: PlayerRepository):
        self.repository = r
        self.playerId = None
        self.playerName = None
        self.password = None

    def setValues(self, id: PlayerId, name: PlayerName, pswd: PlayerPassword):
        self.playerId = id
        self.playerName = name
        self.password = pswd

    def createPlayer(self) -> None:
        """
        プレイヤーを作成
        :return: なし
        """

        # パスワードの暗号化
        cipher = AES.new(self.KEY, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(self.password.getValue().encode('utf-8'))

        # 永続化
        self.repository.addPlayer(
            self.playerId.getValue(),
            self.playerName.getValue(),
            ciphertext,
            tag,
            cipher.nonce
        )

    def authenticatePlayer(self) -> Union[bool, str]:
        """
        プレイヤーの認証
        :return:認証の成否
        """
        player = self.repository.queryPlayer(self.playerId.getValue())

        # 暗号化されたパスワードをKEYで複合し、入力されたパスワード文字列と一致するかチェック
        if player:
            password = player[2].tobytes()
            tag = player[3].tobytes()
            nonce = player[4].tobytes()

            cipher_dec = AES.new(self.KEY, AES.MODE_EAX, nonce)
            dec_password = cipher_dec.decrypt_and_verify(password, tag)

            return dec_password.decode('utf-8') == self.password.getValue(), player[1]

        # IDが存在しない場合
        return False, ''
