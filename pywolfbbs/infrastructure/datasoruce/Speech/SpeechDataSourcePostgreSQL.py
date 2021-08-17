from datetime import datetime

from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.Speech.SpeechRepository import SpeechRepository


class SpeechDataSourcePostgreSQL(SpeechRepository):

    def addSpeech(self, name: str, dt: datetime, title: str, text: str, vil_no: int) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(bulletin_no) FROM bulletins WHERE thread_no = {0}""".format(vil_no))
        no = c.fetchone()[0]
        if not (no is None):
            no = no + 1
        else:
            no = 1

        # textの改行コードに対応
        text = text.replace('\r\n', '<br>')

        c.execute("""INSERT INTO bulletins(bulletin_no, poster_name, post_datetime, post_text, post_title, thread_no)
                    VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')""".format(no, name, dt, text, title, vil_no))
        conn.commit()

        c.close()
        return True
