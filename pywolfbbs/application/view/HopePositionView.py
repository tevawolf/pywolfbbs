import datetime

from flask import redirect, request, url_for, session, flash
from flask.views import MethodView

from pywolfbbs.application.service.VilMemberService import VilMemberService


class HopePositionView(MethodView):
    """
    役職希望View
    """

    @staticmethod
    def post():

        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])
        position = int(request.form['hope_position'])

        VilMemberService.registerHopePosition(vil_no, session['player_id'], position)

        flash('役職希望しました。')

        return redirect(url_for('vil', vil_no=vil_no, disp_date=vil_date))
