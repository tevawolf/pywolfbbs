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
                s.speech_type,
                s.speech_text,
                s.player_id,
                s.vil_no,
                s.vil_date,
                s.member_no,
                s.member_title,
                s.member_name
            FROM speechs s
            WHERE s.vil_no = {0} AND s.vil_date = {1} 
            ORDER BY s.post_datetime ASC
            """.format(no, date)
        )
        rows = c.fetchall()
        speech_list = []
        for row in rows:
            speech_list.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
        c.close()

        return speech_list

    def addSpeech(self, conn, dt: datetime, speech_type: int, text: str, player_id: str, vil_no: int, vil_date
                  , member_no: int, member_title: str, member_name: str) -> bool:

        c = conn.cursor()

        # TODO 単純な「通し番号」ではなく、「日にち:発言種別-連番」の形式で
        c.execute(f"""SELECT MAX(speech_no) FROM speechs WHERE vil_no = {vil_no} AND vil_date = {vil_date}""")
        speech_no = c.fetchone()[0]
        if speech_no is not None:
            speech_no = speech_no + 1
        else:
            speech_no = 1

        # textの改行コードに対応
        text = text.replace('\r\n', '<br>')

        c.execute(f"""INSERT INTO speechs(vil_no, vil_date, speech_no, post_datetime, speech_type, speech_text, 
                    player_id, member_no, member_title, member_name)
                    VALUES ({vil_no}, '{vil_date}', {speech_no}, '{dt}', {speech_type}, '{text}',
                     '{player_id}', {member_no}, '{member_title}', '{member_name}')""")

        c.close()
        return True
