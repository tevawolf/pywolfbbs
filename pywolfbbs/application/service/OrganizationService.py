import random

from flask import url_for

from pywolfbbs.domain.GameVil.object.GameVil import GameVil
from pywolfbbs.domain.GameVil.value.GaveVilNumberOfPeople import GameVilNumberOfPeople
from pywolfbbs.domain.Organization.factory.OrganizationFactory import OrganizationFactory
from pywolfbbs.domain.Organization.object.OrganizationPosition import OrganizationPosition
from pywolfbbs.domain.Position.object.PositionMemberCollection import PositionMemberCollection
from pywolfbbs.domain.VilMember.factory.VilMemberCollectionFactory import VilMemberCollectionFactory
from pywolfbbs.domain.VilMember.object.VilMember import VilMember


class OrganizationService:
    """
    役職編成のサービスオブジェクト
    """
    @staticmethod
    def displayAllPositionOrganization():
        """
        全編成リストを画面出力
        :return:
        """
        pass

    @staticmethod
    def displayHopePositionSelect(organization_no: int, nop: int, hope: int, vil_no: int, vil_date: int) -> str:
        """
        役職希望選択リストを画面出力
        :param organization_no:
        :param nop:
        :param hope:
        :param vil_no
        :param vil_date
        :return:
        """

        organization = OrganizationFactory.create_only_no(organization_no)
        position_list = organization.getHopePositionSelect(GameVilNumberOfPeople(nop))

        html_select = '<label>希望役職</label> \
                        <form action="' + url_for('hope_position') + '" method=post class=""> \
                        <select name="hope_position">'

        html_select += '<option value="99">ランダム(セット済み）</option>'
        html_select += '<option value="98">おまかせ(セット済み）</option>'

        for position in position_list:
            if int(position[0]) == hope:
                html_select += f'<option value="{position[0]}" selected>{position[1]}(セット済み）</option>'
            else:
                html_select += f'<option value="{position[0]}">{position[1]}</option>'

        html_select += f'</select> \
                        <button type="submit" class="btn btn-danger">設定</button><br> \
                        <input type="hidden" name="vil_no" value="{vil_no}"> \
                        <input type="hidden" name="vil_date" value="{vil_date}"> \
                        </form>'

        return html_select

    @staticmethod
    def decideVilOrganizationPosition(conn, vil_today: GameVil):
        """
        村の編成に基づいて参加者の役職を決定する
        :param vil_today:
        :return:
        """
        vil_no = vil_today.vil_no.getValue()

        # 役職ごとの定員をリストで取得
        organization = OrganizationFactory.create_only_no(vil_today.organization_no.getValue())
        organization.setOrganizationPositionsByRepository(vil_today.number_of_people)
        org_position_list = organization.organization_positions

        # 全参加者の希望役職を取得
        members = VilMemberCollectionFactory.create(vil_no)
        members.setVilMemberListByRepository()

        decide_list = []        # 決定役職リスト
        no_decide_list = []    # 未決定役職リスト

        # 役職ごとに処理
        for position in org_position_list:
            # 役職の希望者リストを作成
            hope_position = PositionMemberCollection(position.positionNo)
            hope_position.setMembers(members)
            # 決定者リスト
            decide = PositionMemberCollection(position.positionNo)

            if position.isOverHopeNumber():
                # 希望者数＞定員数の場合

                # ランダムに定員数分の希望者を、決定者リストに入れる
                member_collection = VilMemberCollectionFactory.create(vil_no)
                member_collection.vil_members = random.sample(hope_position.members, position.total.getValue())
                decide.setMembers(member_collection)

                # 選外の希望者を未決定者リストに入れる
                hope_set = set(hope_position.members)
                decide_set = set(decide.members)
                no_decide_list.append(list(hope_set - decide_set))
            else:
                # 希望者数＜＝定員数の場合
                # 希望者リストをそのまま決定者リストに入れる
                member_collection = VilMemberCollectionFactory.create(vil_no)
                member_collection.vil_members = hope_position.members
                decide.setMembers(member_collection)

            # 決定者の役職を確定する
            decide.decideMembersPosition(conn)

            decide_list.append(decide)

        # 未決定役職リストを処理する
        OrganizationService.noDecidePosition(conn, vil_no, org_position_list, decide_list, no_decide_list)

    @staticmethod
    def noDecidePosition(conn, vil_no: int, org_position_list: [OrganizationPosition],
                         decide_list: [PositionMemberCollection], no_decide_list: [VilMember]):

        more_no_decide = []  # まだ未決定のリスト

        # 役職をランダムに選んで処理
        random_choice = random.sample(decide_list, len(decide_list))
        for rand_position in random_choice:
            # 決定者リスト
            decide = PositionMemberCollection(rand_position.positionNo)
            # 役職残り人数
            remain_number = rand_position.getRemainNumber(org_position_list)

            if len(no_decide_list) > remain_number:
                # 未決定者数＞編成役職残り数の場合

                # ランダムに編成役職残り数分の未決定者を、決定者リストに入れる
                member_collection = VilMemberCollectionFactory.create(vil_no)
                member_collection.vil_members = random.sample(no_decide_list, remain_number)
                decide.setMembers(member_collection)
                rand_position.members.extend(decide.members)

                # 選外の希望者を未決定者リストに入れる
                no_decide_set = set(no_decide_list)
                decide_set = set(decide.members)
                more_no_decide.append(list(no_decide_set - decide_set))
            else:
                # 未決定者数＜＝編成役職残り数の場合
                # 未決定者リストをそのまま決定者リストに入れる
                member_collection = VilMemberCollectionFactory.create(vil_no)
                member_collection.vil_members = no_decide_list
                decide.setMembers(member_collection)
                rand_position.members.extend(decide.members)

            # 決定者の役職を確定する
            decide.decideMembersPosition(conn)

        if not more_no_decide:
            return
        else:
            # まだ未決定者が残っている場合は繰り返し
            OrganizationService.noDecidePosition(conn, vil_no, org_position_list, random_choice, more_no_decide)











