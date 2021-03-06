from pywolfbbs.domain.GameVil.value.AbstractGameVilSpeechQuantity import AbstractGameVilSpeechQuantity


class GameVilSpeechNum(AbstractGameVilSpeechQuantity):
    """
    @DomainObject
    @ValueObject
    村発言数
    """

    def __init__(self, num: int):
        _MIN = 0
        _MAX = 100

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

    def isRemain(self) -> bool:
        return self.num != 0
