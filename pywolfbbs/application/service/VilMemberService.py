from pywolfbbs.domain.VilMember.factory.VilMemberFactory import VilMemberFactory


class VilMemberService:
    """
    村参加（キャラクター）情報取得
    村参加登録
    """
    @staticmethod
    def findVilMember(vil_no: int, player_id: str):
        # 参加者番号はダミー
        member = VilMemberFactory.create(vil_no, player_id, 0, 'dummy', 'dummy')
        member.setValuesByRepository()

        if member.isMember():
            return member
        else:
            return None

    @staticmethod
    def joinMember(vil_no: int, player_id: str, member_name: str, member_title: str) -> None:

        member = VilMemberFactory.create(vil_no, player_id, 0, member_name, member_title)
        member.createMember()

        speech
