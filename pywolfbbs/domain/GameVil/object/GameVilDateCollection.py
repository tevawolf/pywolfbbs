import copy

from injector import inject

from pywolfbbs.domain.GameVil.factory.GameVilDateFactory import GameVilDateFactory
from pywolfbbs.domain.GameVil.object.GameVilDate import GameVilDate
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.infrastructure.repository.GameVil.GameVilDateRepository import GameVilDateRepository


class GameVilDateCollection:
    """
    @CollectionObject 村の日付のコレクション
    """
    @inject
    def __init__(self, r: GameVilDateRepository):
        self.repository = r
        self.vil_no = None
        self.dates = []

    def setValues(self, vil_no: GameVilNo):
        """
        セッターメソッド
        :param vil_no:
        :return: なし
        """
        self.vil_no = vil_no

    def setVilDateList(self):
        """
        リポジトリから村の日付のリストを取得し、保持する
        :return: なし
        """
        date_list = self.repository.queryGameVilDateList(self.vil_no.getValue())
        for s in date_list:
            date = GameVilDateFactory.create(s[0], s[2])
            self.dates.append(date)

    def postAllDates(self) -> [GameVilDate]:
        """
        村の日付をすべて提示する
        :return　村の日付リストのコピー
        """
        return copy.deepcopy(self.dates)
