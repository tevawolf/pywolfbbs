import copy

from injector import inject

from pywolfbbs.domain.GameVil.factory.GameVliFactory import GameVliFactory
from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.infrastructure.repository.GameVil.GameFrontRepository import GameFrontRepository


class GameFront:
    """
    @DomainObject ゲームフロント
    @CollectionObject 村のコレクション
    """
    @inject
    def __init__(self, r: GameFrontRepository):
        self.gamevils = []

        # こちらでクエリ発行して、まず全件保持しておく
        vil_list = r.queryGameVilList()
        for b in vil_list:
            vil = GameVliFactory.create(b[0], b[1], b[2], '', b[3], b[4])
            self.gamevils.append(vil)

    def postAllGameVils(self) -> [GameVil]:
        """
        村をすべて表示する
        :return
        """
        return copy.deepcopy(self.gamevils)
