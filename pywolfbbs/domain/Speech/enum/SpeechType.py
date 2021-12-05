import enum


@enum.unique
class SpeechType(enum.Enum):
    """
    @DomainObject 発言種別
    """
    通常発言 = 1
    独り言 = 2
    囁き = 3
    墓下 = 11
    見学 = 12
    村建て発言 = 80
    システム公開メッセージ = 90
    システム非公開メッセージ = 91
    管理人発言 = 100
