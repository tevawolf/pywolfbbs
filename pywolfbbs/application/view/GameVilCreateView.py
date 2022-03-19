from flask import redirect, request, url_for, flash
from flask.views import MethodView

from pywolfbbs.application.service.GameFrontService import GameFrontService
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class GameVilCreateView(MethodView):
    """
    村作成View
    """

    @staticmethod
    def post():

        conn = get_postgres()
        try:
            GameFrontService.createGameVil(conn, request.form['title'], request.form['level'], request.form['vil_password'])
            conn.commit()

            flash('村を作成しました。')

            return redirect(url_for('init'))

        except Exception as e:
            conn.rollback()
            print(e)

