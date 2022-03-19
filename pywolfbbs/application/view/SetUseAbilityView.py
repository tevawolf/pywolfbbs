import datetime

from flask import redirect, request, url_for, session, flash
from flask.views import MethodView

from pywolfbbs.application.service.VilMemberDateStateService import VilMemberDateStateService
from pywolfbbs.application.service.VilMemberService import VilMemberService
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class SetUseAbilityView(MethodView):
    """
    能力行使対象セットView
    """

    @staticmethod
    def post():

        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])
        use_ability_member = int(request.form['use_ability_member'])

        # プレイヤー自身の参加者情報を取得
        player_id = session['player_id']
        self_info = VilMemberService.findVilMemberByPlayerId(vil_no, player_id)

        conn = get_postgres()
        try:
            VilMemberDateStateService.registerSetUseAbility(conn, vil_no, self_info.member_no.getValue(), vil_date, use_ability_member)
            conn.commit()

            flash('XXXXにセットしました。')

            return redirect(url_for('vil', vil_no=vil_no, disp_date=vil_date))

        except Exception as e:
            conn.rollback()
            print(e)
