from flask import flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class _DevProgressDateView_(MethodView):
    """
    開発用　村の日付を進める
    """
    @staticmethod
    def get(vil_no: int):

        conn = get_postgres()
        c = conn.cursor()

        try:
            # 村番号でgamevilsのレコードを取得する
            c.execute("""SELECT * FROM gamevils WHERE vil_no = {0} """.format(vil_no))
            fetch = c.fetchone()
            current_date = int(fetch[4])
            current_date_status = GameVilDateStatus(int(fetch[5]))

            # gamevilsのcurrent_dateを1進める
            c.execute("""UPDATE gamevils SET cur_date = {0} WHERE vil_no = {1}""".format(current_date + 1, vil_no))

            # current_date_statusが1（プロローグ）なら、2（進行中）にする
            if current_date_status == GameVilDateStatus.プロローグ:
                c.execute(
                    """UPDATE gamevils SET cur_date_status = {0} WHERE vil_no = {1}""".format(GameVilDateStatus.進行中.value, vil_no))

            # gamevil_datesに次の日付のレコードを追加する
            c.execute("""INSERT INTO gamevil_dates(date_num, vil_no, date_status)
                        VALUES ({0}, {1}, {2})""".format(current_date + 1, vil_no, GameVilDateStatus.進行中.value))

            # current_date_statusが1（プロローグ）なら、参加者の役職を決定する
            # FIXME ひとまずは希望をそのまま通す
            # TODO 進行中の投票や役職能力セットがつくれたら、編成による定員を考慮する
            # TODO ゲーム開始のシステムメッセージを作成する
            if current_date_status == GameVilDateStatus.プロローグ:
                c.execute("""SELECT player_id, hope_position, member_no FROM vilmembers WHERE vil_no = {0}""".format(vil_no))
                results = c.fetchall()
                for r in results:
                    c.execute("""UPDATE vilmembers SET position = {0} WHERE player_id = '{1}'""".format(r[1], r[0]))
                    # 参加者の状態を作成する
                    c.execute("""INSERT INTO vilmember_date_states(
                    vil_no, member_no, date_num, remain_speech_num, remain_speech_pt, vote_member, use_ability_member)
                                VALUES ({0}, {1}, {2}, {3}, {4}, NULL, NULL)"""
                              .format(vil_no, r[2], current_date + 1, 20, 0))

            # TODO current_date_statusが2（進行中）なら
            # TODO １．処刑を行う　２．襲撃（および護衛）を行う　３，占いを行う　４．霊能を行う
            # TODO 上記対象者、それ以外の翌日の状態を作成する
            # TODO 勝利判定する
            # TODO 翌日のシステムメッセージを作成する

            conn.commit()

            flash('（開発機能）日にちを進めました。')

            return redirect(url_for('vil', vil_no=vil_no, disp_date=current_date + 1))

        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            c.close()


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

        return redirect(url_for('vil', vil_no=vil_no, disp_date=current_date + 1))


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

        return redirect(url_for('vil', vil_no=vil_no, disp_date=current_date + 1))