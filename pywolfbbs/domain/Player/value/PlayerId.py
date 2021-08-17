class PlayerId:
    """
    @DomainObject
    @ValueObject
    プレイヤーID
    """

    def __init__(self, id: str):
        _MIN_LEN = 0
        _MAX_LEN = 20

        if len(id) < _MIN_LEN:
            raise ValueError(
                '{0}は{1}桁以上セットしてください。'.format(
                    self.__class__.__name__, _MIN_LEN)
            )
        if len(id) > _MAX_LEN:
            raise ValueError(
                '{0}は{1}桁以下をセットしてください。'.format(
                    self.__class__, _MAX_LEN)
            )

        self.id = id

    def getValue(self) -> str:
        return self.id

