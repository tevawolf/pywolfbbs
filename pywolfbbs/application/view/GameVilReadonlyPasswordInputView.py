from flask import request, session, flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.application.service.GameVilService import GameVilService


class GameVilReadonlyPasswordInputView(MethodView):

    @staticmethod
    def post():

        no = int(request.form['vil_no'])

        if GameVilService.authenticatePassword(no, request.form['vil_password']):
            session['vil_auth'] = True
            session['vil_auth_no'] = no
            flash('認証成功。スレッドに投稿できるようになりました。')
        else:
            flash('認証失敗。パスワードが違います。')

        return redirect(url_for('vil', no=no))
