from flask import url_for, request, session, flash
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.application.service.PlayerService import PlayerService


class SignInView(MethodView):
    """
    サインインView
    """

    @staticmethod
    def post():

        auth, player_name = PlayerService.signIn(
            request.form['signInId'], request.form['signInPassword']
        )
        if auth:
            session['player_id'] = request.form['signInId']
            session['player_name'] = player_name
            flash('ユーザ{0}でサインインしました。'.format(request.form['signInId']))

            # 村番号と表示日を受け取ってそこに遷移

        else:
            flash('サインインできませんでした。')

        return redirect(url_for('init'))
