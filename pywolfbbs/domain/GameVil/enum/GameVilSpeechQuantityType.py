import enum


@enum.unique
class GameVilSpeechQuantityType(enum.Enum):
    """
    @DomainObject 村の発言数量タイプ
    """
    発言回数制 = 1
    発言pt制 = 2