class PositionName:
    """
    @DomainObject
    @ValueObject
    役職名
    """

    def __init__(self, name: str):
        _MIN = 1
        _MAX = 50

        if len(name) < _MIN:
            raise ValueError(
                '{0}は{1}文字以上をセットしてください。'.format(
                    self.__class__.__name__, _MIN)
            )
        if len(name) > _MAX:
            raise ValueError(
                '{0}は{1}文字以下をセットしてください。'.format(
                    self.__class__, _MAX)
            )

        self.name = name

    def getValue(self) -> str:
        return self.name
