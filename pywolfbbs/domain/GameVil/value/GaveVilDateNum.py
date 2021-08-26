class GameVilDateNum:
    """
    @DomainObject
    @ValueObject
    村日数
    """

    def __init__(self, num: int):
        _MIN = 0
        _MAX = 1000

        if num < _MIN:
            raise ValueError(
                '{0}は{1}以上をセットしてください。'.format(
                    self.__class__.__name__, _MIN)
            )
        if num > _MAX:
            raise ValueError(
                '{0}は{1}以下をセットしてください。'.format(
                    self.__class__, _MAX)
            )

        self.num = num

    def getValue(self) -> int:
        return self.num
