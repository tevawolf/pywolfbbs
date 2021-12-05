from injector import Injector

from pywolfbbs.binds import PositionDIModule
from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition
from pywolfbbs.domain.Position.enum.CampNumbers import CampNumbers
from pywolfbbs.domain.Position.enum.PositionNumbers import PositionNumbers
from pywolfbbs.domain.Position.object.HanterPosition import HanterPosition
from pywolfbbs.domain.Position.object.LunaticPosition import LunaticPosition
from pywolfbbs.domain.Position.object.MediumPosition import MediumPosition
from pywolfbbs.domain.Position.object.SeerPosition import SeerPosition
from pywolfbbs.domain.Position.object.VillagerPosition import VillagerPosition
from pywolfbbs.domain.Position.object.WerewolfPosition import WerewolfPosition
from pywolfbbs.domain.Position.value.AbilityName import AbilityName
from pywolfbbs.domain.Position.value.PositionDescription import PositionDescription
from pywolfbbs.domain.Position.value.PositionIcon import PositionIcon
from pywolfbbs.domain.Position.value.PositionName import PositionName
from pywolfbbs.domain.Position.value.PositionNo import PositionNo


class PositionFactory:

    @staticmethod
    def create(position_no: int, position_name: str, description: str, ability_name:str, icon: str, camps: int) -> AbstractPosition:

        position = None

        injector = Injector([PositionDIModule()])

        if position_no == PositionNumbers.村人.value:
            position = injector.get(VillagerPosition)

        elif position_no == PositionNumbers.人狼.value:
            position = injector.get(WerewolfPosition)

        elif position_no == PositionNumbers.占い師.value:
            position = injector.get(SeerPosition)

        elif position_no == PositionNumbers.霊能者.value:
            position = injector.get(MediumPosition)

        elif position_no == PositionNumbers.狩人.value:
            position = injector.get(HanterPosition)

        elif position_no == PositionNumbers.狂人.value:
            position = injector.get(LunaticPosition)

        else:
            raise NotImplementedError('実装していない役職です')

        position.setValues(
            PositionNo(position_no), PositionName(position_name), PositionDescription(description), AbilityName(ability_name),
            PositionIcon(icon), CampNumbers(camps))
        return position
