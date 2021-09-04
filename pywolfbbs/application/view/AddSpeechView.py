import datetime

from flask import redirect, request, url_for, session, flash
from flask.views import MethodView

from pywolfbbs.application.service.GameVilService import GameVilService


class AddSpeechView(MethodView):
    """
    村への発言投稿View
    """

    @staticmethod
    def post():

        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])

        if 'player_id' in session:
            GameVilService.postSpeech(
                datetime.datetime.now(), request.form['text'], session['player_id'], vil_no, vil_date)
        else:
            # 人狼ゲームでは発言にプレイヤーログイン必須のため、不要になる
            GameVilService.postSpeech(
                datetime.datetime.now(), request.form['text'], 'anonymous', vil_no, vil_date)

        flash('発言を投稿しました。')

        return redirect(url_for('vil', no=vil_no, disp_date=vil_date))
