from injector import Injector

from pywolfbbs.binds import PositionDIModule
from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition
from pywolfbbs.domain.Position.enum.CampNumbers import CampNumbers
from pywolfbbs.domain.Position.enum.PositionNumbers import PositionNumbers
from pywolfbbs.domain.Position.object.VillagerPosition import VillagerPosition
from pywolfbbs.domain.Position.value.PositionDescription import PositionDescription
from pywolfbbs.domain.Position.value.PositionIcon import PositionIcon
from pywolfbbs.domain.Position.value.PositionName import PositionName
from pywolfbbs.domain.Position.value.PositionNo import PositionNo


class PositionFactory:

    @staticmethod
    def create(position_no: int, position_name: str, description: str, icon: str, camps: CampNumbers) -> AbstractPosition:

        injector = Injector([PositionDIModule()])

        if position_no == PositionNumbers.村人.value():
            position = injector.get(VillagerPosition)

        position.setValues(PositionNo(position_no), PositionName(position_name), PositionDescription(description), PositionIcon(icon), camps)
        return position
