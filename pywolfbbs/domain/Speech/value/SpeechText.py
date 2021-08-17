class SpeechText:
    """
    @DomainObject
    @ValueObject
    発言文
    """

    def __init__(self, text: str):
        _MIN = 1
        _MAX = 5000

        if len(text) < _MIN:
            raise ValueError(
                '{0}は{1}文字以上をセットしてください。'.format(
                    self.__class__.__name__, _MIN)
            )
        if len(text) > _MAX:
            raise ValueError(
                '{0}は{1}文字以下をセットしてください。'.format(
                    self.__class__, _MAX)
            )

        self.name = text

    def getValue(self) -> str:
        return self.name
