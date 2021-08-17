class PlayerPassword:
    """
    @DomainObject
    @ValueObject
    プレイヤーPassword
    """

    def __init__(self, password: str):
        _MIN_LEN = 0
        _MAX_LEN = 20

        if len(password) < _MIN_LEN:
            raise ValueError(
                '{0}は{1}桁以上セットしてください。'.format(
                    self.__class__.__name__, _MIN_LEN)
            )
        if len(password) > _MAX_LEN:
            raise ValueError(
                '{0}は{1}桁以下をセットしてください。'.format(
                    self.__class__, _MAX_LEN)
            )

        self.Password = password

    def getValue(self) -> str:
        return self.Password

