import enum


@enum.unique
class SpeechType(enum.Enum):
    """
    @DomainObject 発言種別
    TODO 番号をキーに、文字も持たせる（実際に画面表示してプレイヤーが識別できる文字）
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
