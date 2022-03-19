from pywolfbbs.application.service.OrganizationService import OrganizationService
from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.factory.GameVilDateFactory import GameVilDateFactory
from pywolfbbs.domain.GameVil.factory.GameVilFactory import GameVilFactory
from pywolfbbs.domain.Organization.factory.OrganizationFactory import OrganizationFactory
from pywolfbbs.domain.VilMember.factory.VilMemberCollectionFactory import VilMemberCollectionFactory
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class GameVilUpdateService:
    """
    村の更新サービスオブジェクト
    """

    @staticmethod
    def vilUpdate(vil_no: int) -> int:
        """
        村の更新処理
        :param vil_no:
        :return:
        """
        conn = get_postgres()
        try:

            # 村の基本情報を取得する
            vil_today = GameVilFactory.create_only_no(vil_no)
            vil_today.setValuesByRepository()

            next_date_status = None

            if vil_today.current_date_status.isPrologue():
                # プロローグでの更新処理

                next_date_status = GameVilDateStatus.進行中
                # 参加者の役職を決定する
                OrganizationService.decideVilOrganizationPosition(conn, vil_today)

            else:
                next_date_status = vil_today.current_date_status

            # 村の現在日を1進める
            next_date = vil_today.nextDate(conn, next_date_status)
            vil_nextday = GameVilFactory.create(vil_today.vil_no.getValue(), vil_today.vil_name.getValue(),
                                                vil_today.public_level.value, vil_today.password.getValue(),
                                                next_date.getValue(), next_date_status.value,
                                                vil_today.speech_quantity_type.value,
                                                vil_today.max_speech_quantity.getValue(),
                                                vil_today.organization_no.getValue(), vil_today.number_of_people.getValue())
            # gamevil_datesに次の日付のレコードを追加する

            # 参加者の次の日の状態を作成する

            conn.commit()

            return vil_nextday.current_date.getValue()

        except Exception as e:
            conn.rollback()
            print(e)
