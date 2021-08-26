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

        # 村番号と表示日を受け取ってそこに遷移
        # なければinit（フロントページ）
        return redirect(url_for('init'))
