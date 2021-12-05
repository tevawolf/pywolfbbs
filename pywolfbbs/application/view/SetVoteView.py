import datetime

from flask import redirect, request, url_for, session, flash
from flask.views import MethodView

from pywolfbbs.application.service.VilMemberDateStateService import VilMemberDateStateService
from pywolfbbs.application.service.VilMemberService import VilMemberService


class SetVoteView(MethodView):
    """
    投票セットView
    """

    @staticmethod
    def post():

        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])
        vote_member = int(request.form['vote_member'])

        # プレイヤー自身の参加者情報を取得
        player_id = session['player_id']
        self_info = VilMemberService.findVilMemberByPlayerId(vil_no, player_id)

        VilMemberDateStateService.registerSetVote(vil_no, self_info.member_no.getValue(), vil_date, vote_member)

        flash('XXXXに投票セットしました。')

        return redirect(url_for('vil', vil_no=vil_no, disp_date=vil_date))
