import enum


@enum.unique
class CampNumbers(enum.Enum):
    """
    @DomainObject 陣営番号の固定値
    """
    中立 = 0
    村人 = 1
    人狼 = 2
