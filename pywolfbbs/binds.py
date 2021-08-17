from injector import Module, Binder

from pywolfbbs.infrastructure.datasoruce.GameVil.GameFrontDataSourcePostgreSQL import GameFrontDataSourcePostgreSQL
from pywolfbbs.infrastructure.datasoruce.GameVil.GameVilDataSourcePostgreSQL import \
    GameVilDataSourcePostgreSQL
from pywolfbbs.infrastructure.datasoruce.Speech.SpeechDataSourcePostgreSQL import SpeechDataSourcePostgreSQL
from pywolfbbs.infrastructure.datasoruce.Player.PlayerDataSourcePostgreSQL import PlayerDataSourcePostgreSQL
from pywolfbbs.infrastructure.repository.GameVil.GameFrontRepository import GameFrontRepository
from pywolfbbs.infrastructure.repository.GameVil.GameVilRepository import GameVilRepository
from pywolfbbs.infrastructure.repository.Speech.SpeechRepository import SpeechRepository
from pywolfbbs.infrastructure.repository.Player.PlayerRepository import PlayerRepository


class GameVilDIModule(Module):

    def configure(self, binder: Binder):
        binder.bind(GameFrontRepository, to=GameFrontDataSourcePostgreSQL)
        binder.bind(GameVilRepository, to=GameVilDataSourcePostgreSQL)


class SpeechDIModule(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(SpeechRepository, to=SpeechDataSourcePostgreSQL)


class PlayerDIModule(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(PlayerRepository, to=PlayerDataSourcePostgreSQL)

