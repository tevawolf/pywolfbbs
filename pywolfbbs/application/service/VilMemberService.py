from pywolfbbs.domain.Position.factory.PositionFactory import PositionFactory
from pywolfbbs.domain.VilMember.enum.VilMemberPlaces import VilMemberPlaces
from pywolfbbs.domain.VilMember.factory.VilMemberCollectionFactory import VilMemberCollectionFactory
from pywolfbbs.domain.VilMember.factory.VilMemberDateStateFactory import VilMemberDateStateFactory
from pywolfbbs.domain.VilMember.factory.VilMemberFactory import VilMemberFactory
from pywolfbbs.domain.VilMember.object.VilMember import VilMember
from pywolfbbs.domain.VilMember.object.VilMemberCollection import VilMemberCollection


class VilMemberService:
    """
    村参加者のサービスオブジェクト
    """

    @staticmethod
    def findVilMemberByPlayerId(vil_no: int, player_id: str) -> VilMember:
        """
        プレイヤーIDより村参加（キャラクター）情報取得
        :param vil_no:
        :param player_id:
        :return:
        """
        # 参加者番号、希望役職No、役職Noはダミー
        member = VilMemberFactory.create(vil_no, player_id, 0, 'dummy', 'dummy', 0, 0)
        member.setValuesByRepositoryPlayerId()

        if member.isMember():
            return member
        else:
            return None

    @staticmethod
    def findVilMemberList(vil_no: int) -> VilMemberCollection:
        """
        村参加者リスト取得
        :param vil_no:
        :return:
        """
        member_collection = VilMemberCollectionFactory.create(vil_no)
        member_collection.setVilMemberListByRepository()

        return member_collection

    @staticmethod
    def joinMember(conn, vil_no: int, player_id: str, member_name: str, member_title: str, vil_date: int, type: int, ) -> int:
        """
        村参加登録
        :param vil_no:
        :param player_id:
        :param member_name:
        :param member_title:
        :return: 参加者No
        """
        # 参加者番号、希望役職No、役職Noはダミー
        member = VilMemberFactory.create(vil_no, player_id, 0, member_name, member_title, 0, 0)
        member_no = member.createMember(conn)
        # TODO 将来は村設定から発言種類、初期発言数などをセットする
        date_state = VilMemberDateStateFactory.create(vil_no, member_no, vil_date,
                                                      VilMemberPlaces.地上.value, 20, 0, 0, 0) # 投票先、使用能力先はダミー
        date_state.createVilMemberDateState(conn)

        return member_no

    @staticmethod
    def registerHopePosition(conn, vil_no: int, player_id: str, position: int) -> None:
        """
        役職希望登録
        :param vil_no:
        :param player_id:
        :param position:
        :return:
        """
        # 参加者番号、役職Noはダミー
        member = VilMemberFactory.create(vil_no, player_id, 0, 'dummy', 'dummy', position, 0)
        member.setHopePosition(conn)

    @staticmethod
    def displayPositionDescription(vil_no: int, player_id: str) -> str:
        """
        役職説明欄を出力する
        :param vil_no:
        :param player_id:
        :return:
        """
        # 参加者番号、希望役職No、役職Noはダミー
        member = VilMemberFactory.create(vil_no, player_id, 0, 'dummy', 'dummy', 0, 0)
        member.setValuesByRepositoryPlayerId()
        # 役職No以外ダミー
        position = PositionFactory.create(member.position.getValue(), 'dummy', 'dummy', 'dummy', 'dummy', 0)
        position.setValuesByRepository()

        # FIXME ひとまずDB値をそのまま
        html_description = position.description.getValue()

        return html_description
