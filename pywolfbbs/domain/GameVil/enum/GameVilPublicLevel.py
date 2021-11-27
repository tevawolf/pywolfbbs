import enum


@enum.unique
class GameVilPublicLevel(enum.Enum):
    """
    @DomainObject 掲示板スレッド公開レベル
    """
    公開 = 1
    入村PASS必要 = 2
    閲覧PASS必要 = 3

