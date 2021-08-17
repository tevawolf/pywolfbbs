from typing import Union

from pywolfbbs.domain.Player.factory.PlayerFactory import PlayerFactory


class PlayerService:
    """
    サインアップ
    サインイン
    """

    @staticmethod
    def signUp(id: str, name: str, password: str) -> None:
        player = PlayerFactory.create(id, name, password)
        player.createPlayer()

    @staticmethod
    def signIn(id: str, password: str) -> Union[bool, str]:
        poster = PlayerFactory.create(id, ' ', password)  # PlayerNameにはダミーをセット
        return poster.authenticatePlayer()
