import datetime

from flask import redirect, request, url_for, session, flash
from flask.views import MethodView

from pywolfbbs.application.service.GameVilService import GameVilService
from pywolfbbs.application.service.SpeechService import SpeechService
from pywolfbbs.application.service.VilMemberDateStateService import VilMemberDateStateService
from pywolfbbs.application.service.VilMemberService import VilMemberService
from pywolfbbs.domain.GameVil.enum.GameVilSpeechQuantityType import GameVilSpeechQuantityType
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class AddSpeechView(MethodView):
    """
    村への発言投稿View
    """

    @staticmethod
    def post():

        vil_no = int(request.form['vil_no'])
        vil_date = int(request.form['vil_date'])
        player_id = session['player_id']

        # 自分の参加者情報を取得
        member = VilMemberService.findVilMemberByPlayerId(vil_no, player_id)

        # 発言数 or 発言ptを減らす
        conn = get_postgres()
        try:
            # 村情報を取得
            vil = GameVilService.getVil(vil_no)
            if vil.speech_quantity_type == GameVilSpeechQuantityType.発言回数制:

                if VilMemberDateStateService.reduceSpeechNumber(conn, vil_no, member.member_no.getValue(), vil_date):
                    SpeechService.postSpeech(conn,
                        datetime.datetime.now(), int(request.form['speech_type']), request.form['text'], player_id, vil_no, vil_date,
                        member.member_no.getValue(), member.member_title.getValue(), member.member_name.getValue()
                    )
                    flash('発言を投稿しました。')
                else:
                    flash('発言回数が上限に達しています。本日は発言できません。')

            elif vil.speech_quantity_type == GameVilSpeechQuantityType.発言pt制:
                # TODO 発言ptを減らす
                pass

            conn.commit()

            return redirect(url_for('vil', vil_no=vil_no, disp_date=vil_date))

        except Exception as e:
            conn.rollback()
            print(e)
