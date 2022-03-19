import enum


@enum.unique
class GameVilDateStatus(enum.Enum):
    """
    @DomainObject 村日にちのステータス
    """
    プロローグ = 1
    進行中 = 2
    過去日 = 3
    エピローグ = 4
    終了 = 5

    def __init__(self, status: int):
        self.status = status

    def isPrologue(self) -> bool:
        return self.status == self.プロローグ.value

    def isProgress(self) -> bool:
        return self.status == self.進行中.value

    def isPastDate(self) -> bool:
        return self.status == self.過去日.value

    def isEpilogue(self) -> bool:
        return self.status == self.エピローグ.value

    def isEnd(self) -> bool:
        return self.status == self.終了.value
