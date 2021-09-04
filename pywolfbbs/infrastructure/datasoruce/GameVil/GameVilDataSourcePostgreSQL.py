from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.GameVil.GameVilRepository import GameVilRepository


class GameVilDataSourcePostgreSQL(GameVilRepository):

    def queryGameVil(self, no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM gamevils WHERE vil_no = {0} """.format(no))
        fetch = c.fetchone()
        vil = []
        vil.append(fetch[1])  # vil_name
        vil.append(fetch[2])  # public_level
        vil.append(fetch[4])  # current_date
        vil.append(fetch[5])  # current_date_status
        c.close()

        return vil

    def queryVilDateList(self, no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM gamevil_dates WHERE vil_no = {0} ORDER BY date_num ASC'.format(no))
        rows = c.fetchall()
        date_list = []
        for row in rows:
            date_list.append([row[0], row[1], row[2]])
        c.close()

        return date_list

    def querySpeechList(self, no: int, date: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute(
            """
            SELECT 
                s.speech_no,
                s.post_datetime,
                s.speech_text,
                s.player_id,
                s.vil_no,
                s.vil_date,
                m.member_no,
                m.member_name,
                m.member_title
            FROM speechs s
            INNER JOIN vilmembers m
            ON s.vil_no = m.vil_no
            AND s.player_id = m.player_id
            WHERE s.vil_no = {0} AND s.vil_date = {1} 
            ORDER BY s.post_datetime ASC
            """.format(no, date)
        )
        rows = c.fetchall()
        speech_list = []
        for row in rows:
            speech_list.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
        c.close()

        return speech_list

    def createGameVil(self, name: str, level: int, password: str, date: int, status: int) -> int:

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(vil_no) FROM gamevils""")
        vil_no = c.fetchone()[0]
        if not (vil_no is None):
            vil_no = vil_no + 1
        else:
            vil_no = 1

        # TODO 例外処理　NGならFalseを返す
        c.execute("""INSERT INTO gamevils(vil_no, vil_name, public_level, vil_password, cur_date, cur_date_status)
                    VALUES ({0}, '{1}', {2}, '{3}', {4}, {5})""".format(vil_no, name, str(level), password, date, status))
        conn.commit()

        c.close()
        return vil_no

    def queryGameVilPassword(self, no: int) -> str:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT vil_password FROM gamevils WHERE vil_no = {0}'.format(no))
        db_password = c.fetchone()[0]
        if not (db_password is None):
            return db_password
        else:
            return ''
