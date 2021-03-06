from pywolfbbs.domain.GameVil.value.AbstractGameVilSpeechQuantity import AbstractGameVilSpeechQuantity


class GameVilSpeechPt(AbstractGameVilSpeechQuantity):
    """
    @DomainObject
    @ValueObject
    村発言Pt数
    """

    def __init__(self, num: int):
        _MIN = 0
        _MAX = 10000

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
