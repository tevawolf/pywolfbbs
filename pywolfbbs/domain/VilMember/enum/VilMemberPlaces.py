import enum


@enum.unique
class VilMemberPlaces(enum.Enum):
    """
    @DomainObject 参加者の居場所の固定値
    """
    地上 = 1
    墓下 = 2
    見学 = 3