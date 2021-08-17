from injector import Injector

from pywolfbbs.binds import PlayerDIModule
from pywolfbbs.domain.Player.object.Player import Player
from pywolfbbs.domain.Player.value.PlayerId import PlayerId
from pywolfbbs.domain.Player.value.PlayerName import PlayerName
from pywolfbbs.domain.Player.value.PlayerPassword import PlayerPassword


class PlayerFactory:

    @staticmethod
    def create(id: str, name: str, password: str) -> Player:

        injector = Injector([PlayerDIModule()])
        player = injector.get(Player)
        player.setValues(PlayerId(id), PlayerName(name), PlayerPassword(password))

        return player
