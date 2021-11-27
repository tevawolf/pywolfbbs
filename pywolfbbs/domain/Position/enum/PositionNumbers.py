import enum


@enum.unique
class PositionNumbers(enum.Enum):
    """
    @DomainObject 役職番号の固定値
    """
    ダミー = 0
    村人 = 1
    人狼 = 2
    占い師 = 3
    霊能者 = 4
    狩人 = 5
    狂人 = 6