import copy

from injector import inject

from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.Speech.factory.SpeechFactory import SpeechFactory
from pywolfbbs.domain.Speech.object.Speech import Speech
from pywolfbbs.infrastructure.repository.Speech.SpeechRepository import SpeechRepository


class SpeechCollection:
    """
    @CollectionObject 発言のコレクション
    """
    @inject
    def __init__(self, r: SpeechRepository):
        self.repository = r
        self.vil_no = None
        self.speeches = []

    def setValues(self, vil_no: GameVilNo):
        """
        セッターメソッド
        :param vil_no:
        :return: なし
        """
        self.vil_no = vil_no

    def setSpeechList(self, disp_date: int):
        """
        リポジトリから発言のリストを取得し、保持する
        :return: なし
        """
        speech_list = self.repository.querySpeechList(self.vil_no.getValue(), disp_date)
        for s in speech_list:
            speech = SpeechFactory.create(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9])
            self.speeches.append(speech)

    def postAllSpeeches(self) -> [Speech]:
        """
        発言をすべて提示する
        :return　発言リストのコピー
        """
        return copy.deepcopy(self.speeches)
