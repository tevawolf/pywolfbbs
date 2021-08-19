from datetime import datetime

from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.Speech.SpeechRepository import SpeechRepository


class SpeechDataSourcePostgreSQL(SpeechRepository):

    def addSpeech(self, dt: datetime, text: str, player_id: str, vil_no: int) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(speech_no) FROM speechs WHERE vil_no = {0}""".format(vil_no))
        no = c.fetchone()[0]
        if not (no is None):
            no = no + 1
        else:
            no = 1

        # textの改行コードに対応
        text = text.replace('\r\n', '<br>')

        c.execute("""INSERT INTO speechs(speech_no, post_datetime, speech_text, player_id, vil_no)
                    VALUES ({0}, '{1}', '{2}', '{3}', '{4}')""".format(no, dt, text, player_id, vil_no))
        conn.commit()

        c.close()
        return True
