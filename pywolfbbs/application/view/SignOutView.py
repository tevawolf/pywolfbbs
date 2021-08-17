from flask import url_for, request, session, flash
from flask.views import MethodView
from werkzeug.utils import redirect


class SignOutView(MethodView):
    """
    サインアウトView
    """

    @staticmethod
    def get():

        session.pop('player_id', None)
        session.pop('player_name', None)

        flash('サインアウトしました。')

        return redirect(url_for('init'))