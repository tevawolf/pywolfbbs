from flask import url_for

from pywolfbbs.domain.Position.factory.PositionFactory import PositionFactory
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
        state = VilMemberDateStateFactory.create(vil_no, member_no, date_num, 1, 0, 0, 0, 0)   # キー値以外はダミー
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
        member_state_collection = VilMemberDateStateCollectionFactory.create(vil_no, 0, date_num)   # 参加者Noはダミー
        member_state_collection.setVilMemberDateStateListByDate()

        html_select = ''

        for member_state in member_state_collection.vil_members_date_state:

            # 村番号、参加者No以外はダミー
            member = VilMemberFactory.create(vil_no, 'dummy', member_state.member_no.getValue(), 'dummy', 'dummy', 0, 0)
            member.setValuesByRepositoryMemberNo()

            html_select += f"""
                <div class="card">
                <div class="card-body">
                <label>{member.member_title.getValue()} {member.member_name.getValue()}</label><br>
                <label>残り発言数：{member_state.remain_speech_num.getValue()}回</label>
                </div>
                </div>"""

        return html_select

    @staticmethod
    def displayVoteSelect(vil_no: int, date_num: int, vote: int) -> str:
        """
        村参加者の生存者から投票相手選択フォームを画面出力
        :param vil_no:
        :param date_num:
        :param vote:
        :return:
        """
        # 参加者の状態を取得
        member_state_collection = VilMemberDateStateCollectionFactory.create(vil_no, 100, date_num)
        member_state_collection.setVilMemberDateStateListByDate()

        # 生存者のみに絞り込み
        ground_member_list = []
        for member_state in member_state_collection.vil_members_date_state:
            if member_state.place == VilMemberPlaces.地上:
                ground_member_list.append(member_state)

        # 選択フォームを作成
        html_select = f"""<label>投票先</label>
                        <form action="{url_for('set_vote')}" method=post class="">
                        <select name="vote_member">"""

        for ground_member_state in ground_member_list:

            # 村番号、参加者番号以外はダミー
            ground_member = VilMemberFactory.create(vil_no, 'dummy', ground_member_state.member_no.getValue(), 'dummy', 'dummy', 0, 0)
            ground_member.setValuesByRepositoryMemberNo()

            # その参加者に投票セット済みかどうか
            # TODO ValueObjectにequalsメソッドを追加して判定に使用するようにしたい
            if int(ground_member_state.member_no.getValue()) == vote:

                html_select += f"""<option value="{ground_member.member_no.getValue()}" selected>
                                        {ground_member.member_title.getValue()} {ground_member.member_name.getValue()}(セット済み）
                                    </option>"""
            else:
                html_select += f"""<option value="{ground_member.member_no.getValue()}">
                                        {ground_member.member_title.getValue()} {ground_member.member_name.getValue()}
                                    </option>"""

        html_select += f"""</select>
                        <button type="submit" class="btn btn-danger">セット</button><br>
                        <input type="hidden" name="vil_no" value="{vil_no}">
                        <input type="hidden" name="vil_date" value="{date_num}">
                        </form>"""

        return html_select

    @staticmethod
    def displayUseAbilitySelect(vil_no: int, date_num: int, use: int, position_no: int) -> str:
        """
        村参加者の生存者から能力行使相手選択フォームを画面出力

        :param vil_no:
        :param date_num:
        :param use:
        :param position_no:
        :return:
        """
        # 参加者の状態を取得
        member_state_collection = VilMemberDateStateCollectionFactory.create(vil_no, 100, date_num)
        member_state_collection.setVilMemberDateStateListByDate()

        # 生存者のみに絞り込み
        ground_member_list = []
        for member_state in member_state_collection.vil_members_date_state:
            if member_state.place == VilMemberPlaces.地上:
                ground_member_list.append(member_state)

        # 自分の役職を取得
        position = PositionFactory.create(position_no, 'dummy', 'dummy', 'dummy', 'dummy', 0)     # 役職No以外はダミー
        position.setValuesByRepository()

        # 能力名がなければ、何もフォームを出力しない
        if position.ability_name is None:
            return ''

        # 選択フォームを作成
        html_select = '<label>{0}先</label>'.format(position.ability_name.getValue())
        html_select += f"""<form action="{url_for('set_use_ability')}" method=post class="">
                        <select name="use_ability_member">"""

        for ground_member_state in ground_member_list:

            # 村番号、参加者番号以外はダミー
            ground_member = VilMemberFactory.create(vil_no, 'dummy', ground_member_state.member_no.getValue(), 'dummy', 'dummy', 0, 0)
            ground_member.setValuesByRepositoryMemberNo()

            # その参加者に投票セット済みかどうか
            # TODO ValueObjectにequalsメソッドを追加して判定に使用するようにしたい
            if int(ground_member_state.member_no.getValue()) == use:

                html_select += '<option value="{0}" selected>{1}(セット済み）</option>'\
                    .format(ground_member.member_no.getValue(),
                            ground_member.member_title.getValue() + ' ' + ground_member.member_name.getValue())
            else:
                html_select += '<option value="{0}">{1}</option>'\
                    .format(ground_member.member_no.getValue(),
                            ground_member.member_title.getValue() + ' ' + ground_member.member_name.getValue())

        html_select += '</select> \
                        <button type="submit" class="btn btn-danger">{0}セット</button><br> \
                        <input type="hidden" name="vil_no" value="{1}"> \
                        <input type="hidden" name="vil_date" value="{2}"> \
                        </form>'.format(position.ability_name.getValue(), vil_no, date_num)

        return html_select

    @staticmethod
    def registerSetVote(conn, vil_no: int, member_no: int, date_num: int, vote_member: int) -> None:
        """
        投票セット登録
        :param vil_no:
        :param member_no:
        :param date_num:
        :param vote_member:
        :return:
        """
        # 居場所、発言数、発言pt、能力行使先はダミー
        state = VilMemberDateStateFactory.create(vil_no, member_no, date_num, 1, 0, 0, vote_member, 0)
        state.registerVote(conn)

    @staticmethod
    def registerSetUseAbility(conn, vil_no: int, member_no: int, date_num: int, use_ability_member: int) -> None:
        """
        能力行使セット登録
        :param vil_no:
        :param player_id:
        :param position:
        :return:
        """
        # 居場所、発言数、発言pt、投票先はダミー
        state = VilMemberDateStateFactory.create(vil_no, member_no, date_num, 1, 0, 0, 0, use_ability_member)
        state.registerUseAbility(conn)

    @staticmethod
    def reduceSpeechNumber(conn, vil_no: int, member_no: int, date_num: int) -> bool:
        """
        発言数を減らす
        :param vil_no:
        :param member_no:
        :param date_num:
        :return:
        """
        # 居場所、発言数、発言pt、投票先、能力行使先はダミー
        state = VilMemberDateStateFactory.create(vil_no, member_no, date_num, 1, 0, 0, 0, 0)
        state.setValuesByRepository()
        return state.reduceSpeechNumber(conn)

    # TODO 発言ptを減らす
