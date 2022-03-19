class PositionNo:
    """
    @DomainObject
    @ValueObject
    役職番号
    """

    def __init__(self, no: int):
        _MIN = 0
        _MAX = 100

        if no < _MIN:
            raise ValueError(
                '{0}は{1}以上をセットしてください。'.format(
                    self.__class__.__name__, _MIN)
            )
        if no > _MAX:
            raise ValueError(
                '{0}は{1}以下をセットしてください。'.format(
                    self.__class__, _MAX)
            )

        self.no = no

    def getValue(self) -> int:
        return self.no

    def isNotZero(self) -> bool:
        return self.no != 0

    def equalNumber(self, no: 'PositionNo'):
        return no.getValue() == self.no
