from injector import Injector

from pywolfbbs.binds import GameVilDIModule
from pywolfbbs.domain.GameVil.enum.GameVilSpeechQuantityType import GameVilSpeechQuantityType
from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.enum.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.domain.GameVil.value.GameVilName import GameVilName
from pywolfbbs.domain.GameVil.value.GameVilNo import GameVilNo
from pywolfbbs.domain.GameVil.value.GameVilPassword import GameVilPassword
from pywolfbbs.domain.GameVil.value.GameVilSpeechNum import GameVilSpeechNum
from pywolfbbs.domain.GameVil.value.GameVilSpeechPt import GameVilSpeechPt
from pywolfbbs.domain.GameVil.value.GaveVilDateNum import GameVilDateNum
from pywolfbbs.domain.GameVil.value.GaveVilNumberOfPeople import GameVilNumberOfPeople
from pywolfbbs.domain.Organization.value.OrganizationNo import OrganizationNo


class GameVilFactory:

    @staticmethod
    def create(no: int, name: str, level: int, password: str, date: int, status: int, speech_type: int, max_speech: int, organization: int, people: int) -> GameVil:

        injector = Injector([GameVilDIModule()])
        vil = injector.get(GameVil)
        if speech_type == GameVilSpeechQuantityType.発言回数制.value:

            vil.setValues(GameVilNo(no), GameVilName(name), GameVilPublicLevel(level), GameVilPassword(password),
                          GameVilDateNum(date), GameVilDateStatus(status),
                          GameVilSpeechQuantityType(speech_type), GameVilSpeechNum(max_speech),
                          OrganizationNo(organization), GameVilNumberOfPeople(people))

        elif speech_type == GameVilSpeechQuantityType.発言pt制.value:

            vil.setValues(GameVilNo(no), GameVilName(name), GameVilPublicLevel(level), GameVilPassword(password),
                          GameVilDateNum(date), GameVilDateStatus(status),
                          GameVilSpeechQuantityType(speech_type), GameVilSpeechPt(max_speech),
                          OrganizationNo(organization), GameVilNumberOfPeople(people))

        return vil

    @staticmethod
    def create_only_no(no: int):
        # 公開レベル、現在日、現在日ステータス、発言タイプ、最大発言数量、編成No、人数もダミー
        return GameVilFactory.create(no, 'name', GameVilPublicLevel.公開.value, 'password', 0,
                                    GameVilDateStatus.プロローグ.value, GameVilSpeechQuantityType.発言回数制.value, 0, 0, 0)

