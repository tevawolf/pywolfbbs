from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.GameVil.GameVilRepository import GameVilRepository


class GameVilDataSourcePostgreSQL(GameVilRepository):

    def queryGameVil(self, no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM threads WHERE thread_no = {0} """.format(no))
        fetch = c.fetchone()
        vil = []
        vil.append(fetch[1])  # vil_name
        vil.append(fetch[2])  # public_level
        c.close()

        return vil

    def querySpeechList(self, no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM bulletins WHERE thread_no = {0} ORDER BY bulletin_no DESC'.format(no))
        rows = c.fetchall()
        speech_list = []
        for row in rows:
            speech_list.append([row[0], row[1], row[2], row[4], row[3], row[5]])
        c.close()

        return speech_list

    def createGameVil(self, name: str, level: int, password: str) -> bool:

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(thread_no) FROM threads""")
        no = c.fetchone()[0]
        if not (no is None):
            no = no + 1
        else:
            no = 1

        # TODO 例外処理　NGならFalseを返す
        c.execute("""INSERT INTO threads(thread_no, thread_name, public_level, thread_password)
                    VALUES ({0}, '{1}', {2}, '{3}')""".format(no, name, str(level), password))
        conn.commit()

        c.close()
        return True

    def queryGameVilPassword(self, no: int) -> str:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT thread_password FROM threads WHERE thread_no = {0}'.format(no))
        db_password = c.fetchone()[0]
        if not (db_password is None):
            return db_password
        else:
            return ''
