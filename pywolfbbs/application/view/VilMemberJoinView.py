from flask import request, session, flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.application.service.VilMemberService import VilMemberService


class VilMemberJoinView(MethodView):

    @staticmethod
    def post():
        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])
        member_title = request.form['member_title']
        member_name = request.form['member_name']

        VilMemberService.joinMember(vil_no, session['player_id'], member_name, member_title)

        flash('入村しました。')

        return redirect(url_for('vil', no=vil_no, disp_date=vil_date))
