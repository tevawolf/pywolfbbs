import datetime

from flask import request, session, flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.application.service.GameVilService import GameVilService
from pywolfbbs.application.service.VilMemberService import VilMemberService


class VilMemberJoinView(MethodView):

    @staticmethod
    def post():
        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])
        member_title = request.form['member_title']
        member_name = request.form['member_name']
        text = request.form['text']
        player_id = session['player_id']

        VilMemberService.joinMember(vil_no, player_id, member_name, member_title)

        GameVilService.postSpeech(
            datetime.datetime.now(), text, player_id, vil_no, vil_date, member_title, member_name)

        flash('入村しました。')

        return redirect(url_for('vil', vil_no=vil_no, disp_date=vil_date))
