from flask import url_for

from pywolfbbs.domain.Position.object.AbstractPosition import AbstractPosition
from pywolfbbs.domain.VilMember.enum.VilMemberPlaces import VilMemberPlaces
from pywolfbbs.domain.VilMember.factory.VilMemberDateStateCollectionFactory import VilMemberDateStateCollectionFactory
from pywolfbbs.domain.VilMember.factory.VilMemberDateStateFactory import VilMemberDateStateFactory
from pywolfbbs.domain.VilMember.factory.VilMemberFactory import VilMemberFactory
from pywolfbbs.domain.VilMember.object.VilMemberDateState import VilMemberDateState


class VilMemberDateStateService:
    """
    村参加者のその日の状態に関するサービスオブジェクト
    """
    @staticmethod
    def findVilMemberDateState(vil_no: int, member_no: int, date_num: int) -> VilMemberDateState:
        """
        村参加者のその日の状態取得
        :param vil_no:
        :param member_no:
        :param date_num:
        :return:
        """
        # キー値以外はダミー
        state = VilMemberDateStateFactory.create(vil_no, member_no, date_num, 0, 0, 0, 0)
        state.setValuesByRepository()

        return state

    @staticmethod
    def displayVilMemberDateStateList(vil_no: int, date_num: int) -> str:
        """
        村参加者のその日の状態リスト（フィルタ機能）を画面出力
        :param vil_no:
        :param date_num
        :return:
        """
        # 参加者Noはダミー
        member_state_collection = VilMemberDateStateCollectionFactory.create(vil_no, 0, date_num)
        member_state_collection.setVilMemberDateStateListByDate()

        html_select = ''

        for member_state in member_state_collection.vil_members_date_state:

            # 村番号、参加者No以外はダミー
            member = VilMemberFactory.create(vil_no, 'dummy', member_state.member_no.getValue(), 'dummy', 'dummy', 0, 0)
            member.setValuesByRepositoryMemberNo()

            html_select += '<div class="card"> \
                <div class="card-body"> \
                <label>{0} {1}</label><br> \
                <label>残り発言数：{2}回</label> \
                </div> \
                </div>'.format(
                member.member_title.getValue(), member.member_name.getValue(), member_state.remain_speech_num.getValue()
            )

        return html_select

    @staticmethod
    def displayVoteSelect(vil_no: int, date_num: int, vote: int) -> str:
        """
        村参加者の生存者から投票相手選択リストを画面出力
        :param vil_no:
        :param date_num:
        :param vote:
        :return:
        """
        member_state_collection = VilMemberDateStateCollectionFactory.create(vil_no, 100, date_num)
        member_state_collection.setVilMemberDateStateListByDate()

        ground_member_list = []
        for member_state in member_state_collection.vil_members_date_state:
            if member_state.place == VilMemberPlaces.地上:
                ground_member_list.append(member_state)

        html_select = '<label>投票先</label> \
                        <form action="' + url_for('vote') + '" method=post class=""> \
                        <select name="vote">'

        for ground_member_state in ground_member_list:

            ground_member = VilMemberFactory.create(vil_no, 'dummy', ground_member_state.member_no.getValue(), '', '', 0)
            ground_member.setValuesByRepositoryMemberNo()

            # TODO ValueObjectにequalsメソッドを追加して判定に使用するようにしたい
            if int(ground_member_state.member_no.getValue()) == vote:

                html_select += '<option value="{0}" selected>{1}(セット済み）</option>'\
                    .format(ground_member.member_no.getValue(),
                            ground_member.member_title.getValue() + ' ' + ground_member.member_name.getValue())
            else:
                html_select += '<option value="{0}">{1}</option>'\
                    .format(ground_member.member_no.getValue(),
                            ground_member.member_title.getValue() + ' ' + ground_member.member_name.getValue())

        html_select += '</select> \
                        <button type="submit" class="btn btn-danger">設定</button><br> \
                        <input type="hidden" name="vil_no" value="{0}"> \
                        <input type="hidden" name="vil_date" value="{1}"> \
                        </form>'.format(vil_no, date_num)

        return html_select

    @staticmethod
    def displayUseAbilitySelect(vil_no: int, date_num: int, position: AbstractPosition) -> str:
        """
        村参加者の生存者から能力行使相手選択リストを画面出力

        :param vil_no:
        :param date_num:
        :param position:
        :return:
        """
        pass

