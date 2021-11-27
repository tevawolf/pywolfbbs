from abc import ABCMeta, abstractmethod

from pywolfbbs.domain.Position.enum.CampNumbers import CampNumbers
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
    def __init__(self, r: PositionRepository):
        self.repository = r
        self.position_no = None # 役職番号
        self.position_name = None   # 役職名
        self.description = None # 役職説明
        self.icon = None
        self.camps = None   # 陣営

    def setValues(self, no: PositionNo, name: PositionName, desc: PositionDescription,
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
        self.icon = icon
        self.camps = camp

    def setValuesByRepository(self) -> None:
        """
        DB取得値をセット
        :return: なし
        """

    # これはVilMemberのリストを使ってGameVilが行う仕事
    # @abstractmethod
    # def displaySelectMember(self, member_list: [VilMember]):
    #     """
    #     能力行使対象選択リストを画面出力
    #     :param member_list:
    #     :return:
    #     """
    #     pass

    @abstractmethod
    def displayDescription(self):
        """
        役職説明を画面出力
        :return:
        """
        pass

    @abstractmethod
    def useAbility(self, src: VilMember, dst: VilMember):
        """
        能力行使。更新処理で呼び出す。
        :param src:
        :param dst:
        :return:
        """
        pass

