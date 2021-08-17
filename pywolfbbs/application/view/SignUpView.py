from flask import request, url_for, session, flash
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.application.service.PlayerService import PlayerService


class SignUpView(MethodView):
    """
    サインアップView
    """

    @staticmethod
    def play():

        PlayerService.signUp(
            request.form['playerId'], request.form['playerName'], request.form['playerPassword']
        )

        # サインインも同時に行う
        session['player_id'] = request.form['playerId']
        session['player_name'] = request.form['playerName']

        flash('ユーザ{0}：{1}でサインアップしました。'.format(request.form['playerId'], request.form['playerName']))

        return redirect(url_for('init'))
