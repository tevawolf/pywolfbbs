from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition
from pywolfbbs.domain.VilMember.object.VilMember import VilMember


class MediumPosition(AbstractPosition):
    """
    霊能者（役職）
    """
    def useAbility(self, src: VilMember, dst: VilMember):
        print('use ability')
