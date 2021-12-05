from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition
from pywolfbbs.domain.VilMember.object.VilMember import VilMember


class HanterPosition(AbstractPosition):
    """
    狩人（役職）
    """
    def useAbility(self, src: VilMember, dst: VilMember):
        print('use ability')
