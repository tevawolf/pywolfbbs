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