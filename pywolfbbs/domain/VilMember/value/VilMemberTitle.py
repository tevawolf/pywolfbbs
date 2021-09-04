class VilMemberTitle:
    """
    @DomainObject
    @ValueObject
    村参加者（キャラクター）肩書き
    """

    def __init__(self, title: str):
        _MIN = 1
        _MAX = 50

        if len(title) < _MIN:
            raise ValueError(
                '{0}は{1}文字以上をセットしてください。'.format(
                    self.__class__.__name__, _MIN)
            )
        if len(title) > _MAX:
            raise ValueError(
                '{0}は{1}文字以下をセットしてください。'.format(
                    self.__class__, _MAX)
            )

        self.name = title

    def getValue(self) -> str:
        return self.name
