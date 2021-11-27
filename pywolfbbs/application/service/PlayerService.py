from typing import Union

from pywolfbbs.domain.Player.factory.PlayerFactory import PlayerFactory


class PlayerService:
    """
    プレイヤーのサービスオブジェクト
    """

    @staticmethod
    def signUp(id: str, name: str, password: str) -> None:
        """
        サインアップ
        :param id:
        :param name:
        :param password:
        :return:
        """
        player = PlayerFactory.create(id, name, password)
        player.createPlayer()

    @staticmethod
    def signIn(id: str, password: str) -> Union[bool, str]:
        """
        サインイン
        :param id:
        :param password:
        :return:
        """
        poster = PlayerFactory.create(id, ' ', password)  # PlayerNameにはダミーをセット
        return poster.authenticatePlayer()
