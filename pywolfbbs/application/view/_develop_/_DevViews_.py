from flask import flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class _DevProgressDateView_(MethodView):
    """
    開発用　村の日付を進める
    """
    @staticmethod
    def get(vil_no: int):

        conn = get_postgres()

        # 村番号でgamevilsのレコードを取得する
        c = conn.cursor()
        c.execute("""SELECT * FROM gamevils WHERE vil_no = {0} """.format(vil_no))
        fetch = c.fetchone()
        current_date = int(fetch[4])

        # gamevilsのcurrent_dateを1進める
        c.execute("""UPDATE gamevils SET cur_date = {0} WHERE vil_no = {1}""".format(current_date + 1, vil_no))

        # current_dateが0だったなら、current_date_statusを2（進行中）にする
        if current_date == 0:
            c.execute(
                """UPDATE gamevils SET cur_date_status = {0} WHERE vil_no = {1}""".format(GameVilDateStatus.進行中.value, vil_no))

        # gamevil_datesに次の日付のレコードを追加する
        c.execute("""INSERT INTO gamevil_dates(date_num, vil_no, date_status)
                    VALUES ({0}, {1}, {2})""".format(current_date + 1, vil_no, GameVilDateStatus.進行中.value))
        conn.commit()
        c.close()

        flash('（開発機能）日にちを進めました。')

        return redirect(url_for('vil', no=vil_no, disp_date=current_date + 1))


class _DevProgressEpilogueView_(MethodView):
    """
    開発用　エピローグに進める
    """
    @staticmethod
    def get(vil_no: int):

        conn = get_postgres()

        # 村番号でgamevilsのレコードを取得する
        c = conn.cursor()
        c.execute("""SELECT * FROM gamevils WHERE vil_no = {0} """.format(vil_no))
        fetch = c.fetchone()
        current_date = int(fetch[4])

        # gamevilsのcurrent_dateを1進める
        # current_date_statusを4（エピローグ）にする
        c.execute(
            """UPDATE gamevils SET cur_date = {0}, cur_date_status = {1} WHERE vil_no = {2}""".format(
                current_date + 1, GameVilDateStatus.エピローグ.value, vil_no))

        # gamevil_datesに次の日付のレコードを追加する
        c.execute("""INSERT INTO gamevil_dates(date_num, vil_no, date_status)
                    VALUES ({0}, {1}, {2})""".format(current_date + 1, vil_no, GameVilDateStatus.エピローグ.value))
        conn.commit()
        c.close()

        flash('（開発機能）エピローグに進めました。')

        return redirect(url_for('vil', no=vil_no, disp_date=current_date + 1))


class _DevProgressEndView_(MethodView):
    """
    開発用　村を終了する
    """

    @staticmethod
    def get(vil_no: int):
        conn = get_postgres()

        # 村番号でgamevilsのレコードを取得する
        c = conn.cursor()
        c.execute("""SELECT * FROM gamevils WHERE vil_no = {0} """.format(vil_no))
        fetch = c.fetchone()
        current_date = int(fetch[4])

        # gamevilsのcurrent_dateを1進める
        # current_date_statusを5（終了）にする
        c.execute(
            """UPDATE gamevils SET cur_date = {0}, cur_date_status = {1} WHERE vil_no = {2}""".format(
                current_date + 1, GameVilDateStatus.終了.value, vil_no))

        # gamevil_datesに次の日付のレコードを追加する
        c.execute("""INSERT INTO gamevil_dates(date_num, vil_no, date_status)
                    VALUES ({0}, {1}, {2})""".format(current_date + 1, vil_no, GameVilDateStatus.終了.value))
        conn.commit()
        c.close()

        flash('（開発機能）村を終了しました。')

        return redirect(url_for('vil', no=vil_no, disp_date=current_date + 1))