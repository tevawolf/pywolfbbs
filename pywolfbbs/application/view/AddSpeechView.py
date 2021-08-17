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

        if 'player_name' in session:
            GameVilService.postSpeech(
                session['player_name'], datetime.datetime.now(), request.form['title'], request.form['text'], vil_no)
        else:
            GameVilService.postSpeech(
                'ななしさん', datetime.datetime.now(), request.form['title'], request.form['text'], vil_no)

        flash('スレッドに投稿しました。')

        return redirect(url_for('vil', no=vil_no))
