import datetime

from flask import request, session, flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.application.service.SpeechService import SpeechService
from pywolfbbs.application.service.VilMemberService import VilMemberService
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class VilMemberJoinView(MethodView):

    @staticmethod
    def post():
        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])
        speech_type = int(request.form['speech_type'])
        member_title = request.form['member_title']
        member_name = request.form['member_name']
        text = request.form['text']
        player_id = session['player_id']

        conn = get_postgres()
        try:
            member_no = VilMemberService.joinMember(conn, vil_no, player_id, member_name, member_title, vil_date, speech_type)

            SpeechService.postSpeech(conn,
                datetime.datetime.now(), speech_type, text, player_id, vil_no, vil_date, member_no, member_title, member_name)

            conn.commit()

            flash('入村しました。')

            return redirect(url_for('vil', vil_no=vil_no, disp_date=vil_date))

        except Exception as e:
            conn.rollback()
            print(e)

