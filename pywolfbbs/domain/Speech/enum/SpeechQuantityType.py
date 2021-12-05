import enum


@enum.unique
class SpeechQuantityType(enum.Enum):
    """
    @DomainObject 発言数量タイプ
    """
    回数制 = 1
    pt制 = 2
