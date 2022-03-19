from flask import flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from pywolfbbs.application.service.GameVilUpdateService import GameVilUpdateService
from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres


class _DevProgressDateView_(MethodView):
    """
    開発用　村の日付を進める
    """
    @staticmethod
    def get(vil_no: int):

        next_date = GameVilUpdateService.vilUpdate(vil_no)

        flash('（開発機能）日にちを進めました。')

        return redirect(url_for('vil', vil_no=vil_no, disp_date=next_date))

        # conn = get_postgres()
        # c = conn.cursor()
        #
        # try:
        #     # 村番号でgamevilsのレコードを取得する
        #     c.execute("""SELECT * FROM gamevils WHERE vil_no = {0} """.format(vil_no))
        #     vil = c.fetchone()
        #     current_date = int(vil[4])
        #     current_date_status = GameVilDateStatus(int(vil[5]))
        #
        #     next_date = current_date + 1
        #     next_date_status = None
        #
        #     if current_date_status == GameVilDateStatus.プロローグ:
        #
        #         next_date_status = GameVilDateStatus.進行中.value
        #
        #         c.execute("""SELECT player_id, hope_position, member_no FROM vilmembers WHERE vil_no = {0}""".format(vil_no))
        #         hopes = c.fetchall()
        #         """
        #         TODO 参加者の役職を決定する：編成による定員を考慮する
        #         【仕様】
        #         １．役職ごとに希望者リストを作成
        #         ２．役職ごとの定員を取得し、希望者リストからランダムで定員数分を選択し、役職決定する
        #         ３．希望が通らなかった参加者は参加者Noの若い順に、1.村人、２．人狼、３．村人陣営の空き役職者に役職Noの若い順、４．人狼陣営の空き役職者に役職Noの若い順
        #         """
        #         # １．役職ごとに希望者リストを作成
        #         hope_dict = {}
        #         for hope in hopes:
        #             if hope[1] in hope_dict:
        #                 hope_dict[hope[1]].append([hope[0],hope[2]])
        #             else:
        #                 hope_dict[hope[1]] = [[hope[0],hope[2]]]
        #         # ２．役職ごとの定員を取得し、希望者リストからランダムで定員数分を選択し、役職決定する
        #         # 2.1. 役職ごとの定員を取得
        #         organization_no = vil[8]
        #         number_of_people = vil[9]
        #         c.execute("""SELECT position_no, total FROM organization_positions WHERE organization_no = {0} AND number_of_people = {1}""".format(organization_no, number_of_people))
        #         vil_positions = c.fetchall()
        #         # 2.2.1. 希望者リストのサイズが定員以内なら、そのまま希望どおりの役職に決定する。
        #         # 2.2.2. 希望者リストのサイズが定員より大きいなら、そこからランダムで定員数分を選択
        #         # 2.2.3. 希望が通らなかったPLを保持し、人数が埋まっていない役職に順次決定していく
        #         # TODO ランダムやおまかせの仕様決め、考慮して実装
        #         # TODO まず紙でフローチャートを書いてアルゴリズムを作成すること
        #         for position in vil_positions:
        #             position_no = position[0]   # 役職番号
        #             total = int(position[1])         # 定員
        #             hope_list = hope_dict[position_no]  # [[player_id, member_no],...]
        #
        #             for hope in hope_list:
        #                 c.execute("""UPDATE vilmembers SET position = {0} WHERE vil_no = {1} AND player_id = '{2}'""".format(position_no, vil_no, hope[0]))
        #                 # 参加者の状態を作成する
        #                 c.execute("""INSERT INTO vilmember_date_states(
        #                 vil_no, member_no, date_num, remain_speech_num, remain_speech_pt, vote_member, use_ability_member)
        #                             VALUES ({0}, {1}, {2}, {3}, {4}, NULL, NULL)"""
        #                           .format(vil_no, hope[1], current_date + 1, 20, 0))
        #
        #         # TODO ゲーム開始のシステムメッセージを作成する
        #
        #     elif current_date_status == GameVilDateStatus.進行中:
        #         # TODO １．処刑を行う
        #         # 投票の集計・最多票の判定　同数者はランダム判定
        #         # 最多票の参加者の翌日のステータスを死亡・墓下へ
        #         # TODO ２．襲撃（および護衛）を行う
        #         # 襲撃セットの集計・最多票の判定　同数者はランダム判定
        #         # TODO ３，占いを行う
        #         # TODO ４．霊能を行う
        #         # TODO 上記対象者、それ以外の翌日の状態を作成する
        #         # TODO 勝利判定する
        #
        #         next_date_status = GameVilDateStatus.進行中.value
        #
        #         next_date_status = GameVilDateStatus.エピローグ.value
        #
        #         # TODO 翌日のシステムメッセージを作成する
        #
        #     elif current_date_status == GameVilDateStatus.エピローグ:
        #         next_date_status = GameVilDateStatus.終了.value
        #
        #     # gamevilsのcurrent_dateを1進める
        #     c.execute("""UPDATE gamevils SET cur_date = {0} , cur_date_status = {1} WHERE vil_no = {2}""".format(
        #         next_date, next_date_status, vil_no))
        #     # gamevil_datesに次の日付のレコードを追加する
        #     c.execute("""INSERT INTO gamevil_dates(date_num, vil_no, date_status)
        #                 VALUES ({0}, {1}, {2})""".format(current_date + 1, vil_no, next_date_status))
        #
        #     conn.commit()
        #
        #     flash('（開発機能）日にちを進めました。')
        #
        #     return redirect(url_for('vil', vil_no=vil_no, disp_date=current_date + 1))
        #
        # except Exception as e:
        #     conn.rollback()
        #     print(e)
        # finally:
        #     c.close()


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