from datetime import datetime

from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.Speech.SpeechRepository import SpeechRepository


class SpeechDataSourcePostgreSQL(SpeechRepository):

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

    def addSpeech(self, dt: datetime, text: str, player_id: str, vil_no: int, vil_date
                  , member_title: str, member_name: str) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(speech_no) FROM speechs WHERE vil_no = {0}""".format(vil_no))
        no = c.fetchone()[0]
        if no is not None:
            no = no + 1
        else:
            no = 1

        # textの改行コードに対応
        text = text.replace('\r\n', '<br>')

        c.execute("""INSERT INTO speechs(speech_no, post_datetime, speech_text, player_id, vil_no, vil_date
                    , member_title, member_name)
                    VALUES ({0}, '{1}', '{2}', '{3}', {4}, {5}, {6}, {7})""".format(
            no, dt, text, player_id, vil_no, vil_date, member_title, member_name))
        conn.commit()

        c.close()
        return True
