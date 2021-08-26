import datetime

from flask import redirect, request, url_for, flash
from flask.views import MethodView

from pywolfbbs.application.service.GameFrontService import GameFrontService


class GameVilCreateView(MethodView):
    """
    村作成View
    """

    @staticmethod
    def post():

        GameFrontService.createGameVil(request.form['title'], request.form['level'], request.form['vil_password'])

        flash('村を作成しました。')

        return redirect(url_for('init'))
