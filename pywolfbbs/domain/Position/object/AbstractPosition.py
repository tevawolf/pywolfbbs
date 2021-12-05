from abc import ABCMeta, abstractmethod

from injector import inject

from pywolfbbs.domain.Position.enum.CampNumbers import CampNumbers
from pywolfbbs.domain.Position.value.AbilityName import AbilityName
from pywolfbbs.domain.Position.value.PositionDescription import PositionDescription
from pywolfbbs.domain.Position.value.PositionIcon import PositionIcon
from pywolfbbs.domain.Position.value.PositionName import PositionName
from pywolfbbs.domain.Position.value.PositionNo import PositionNo
from pywolfbbs.domain.VilMember.object.VilMember import VilMember
from pywolfbbs.infrastructure.repository.Position.PositionRepository import PositionRepository


class AbstractPosition(metaclass=ABCMeta):

    """
    @DomainObject 役職を表す抽象クラス
    """
    @inject
    def __init__(self, r: PositionRepository):
        self.repository = r
        self.position_no = None # 役職番号
        self.position_name = None   # 役職名
        self.description = None # 役職説明
        self.ability_name = None    # 能力名
        self.icon = None
        self.camps = None   # 陣営

    def setValues(self, no: PositionNo, name: PositionName, desc: PositionDescription, ability: AbilityName,
                  icon: PositionIcon, camp: CampNumbers) -> None:
        """
        セッターメソッド
        :param no:
        :param name:
        :param desc:
        :param icon:
        :param camp:
        :return: なし
        """
        self.position_no = no
        self.position_name = name
        self.description = desc
        self.ability_name = ability
        self.icon = icon
        self.camps = camp

    def setValuesByRepository(self) -> None:
        """
        DB取得値をセット
        :return: なし
        """
        position = self.repository.queryPositionById(self.position_no.getValue())

        if position:
            self.position_name = PositionName(position[0])
            self.description = PositionDescription(position[1])
            if position[2] is not None:
                self.ability_name = AbilityName(position[2])
            else:
                self.ability_name = None
            self.camps = CampNumbers(position[3])

    @abstractmethod
    def useAbility(self, src: VilMember, dst: VilMember):
        """
        能力行使。更新処理で呼び出す。
        :param src:
        :param dst:
        :return:
        """
        pass

