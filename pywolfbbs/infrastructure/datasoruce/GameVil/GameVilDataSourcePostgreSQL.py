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
        c.close()

        return vil

    def querySpeechList(self, no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM speechs WHERE vil_no = {0} ORDER BY vil_no ASC'.format(no))
        rows = c.fetchall()
        speech_list = []
        for row in rows:
            speech_list.append([row[0], row[1], row[2], row[3], row[4]])
        c.close()

        return speech_list

    def createGameVil(self, name: str, level: int, password: str) -> bool:

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(vil_no) FROM gamevils""")
        no = c.fetchone()[0]
        if not (no is None):
            no = no + 1
        else:
            no = 1

        # TODO 例外処理　NGならFalseを返す
        c.execute("""INSERT INTO gamevils(vil_no, vil_name, public_level, vil_password)
                    VALUES ({0}, '{1}', {2}, '{3}')""".format(no, name, str(level), password))
        conn.commit()

        c.close()
        return True

    def queryGameVilPassword(self, no: int) -> str:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT vil_password FROM gamevils WHERE vil_no = {0}'.format(no))
        db_password = c.fetchone()[0]
        if not (db_password is None):
            return db_password
        else:
            return ''
