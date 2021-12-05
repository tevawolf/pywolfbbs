from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.GameVil.GameVilRepository import GameVilRepository


class GameVilDataSourcePostgreSQL(GameVilRepository):

    def queryGameVil(self, no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM gamevils WHERE vil_no = {0} """.format(no))
        fetch = c.fetchone()
        vil = [fetch[1], fetch[2], fetch[4], fetch[5], fetch[6], fetch[7]]
        c.close()

        return vil

    def queryGameVilList(self) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM gamevils ORDER BY vil_no DESC')
        rows = c.fetchall()
        thread_list = []
        for row in rows:
            thread_list.append([row[0], row[1], row[2], row[4], row[5], row[6], row[7]])
        c.close()

        return thread_list

    def createGameVil(self, name: str, level: int, password: str, date: int, status: int, speech_type: int
                      , organization: int) -> int:

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(vil_no) FROM gamevils""")
        vil_no = c.fetchone()[0]
        if  vil_no is not None:
            vil_no = vil_no + 1
        else:
            vil_no = 1

        # TODO 例外処理　NGならFalseを返す
        c.execute("""INSERT INTO gamevils(
        vil_no, vil_name, public_level, vil_password, cur_date, cur_date_status, speech_quantity_type, organization_no)
                    VALUES ({0}, '{1}', {2}, '{3}', {4}, {5}, {6}, {7})"""
                  .format(vil_no, name, str(level), password, date, status, speech_type, organization))
        conn.commit()

        c.close()
        return vil_no

    def queryGameVilPassword(self, no: int) -> str:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT vil_password FROM gamevils WHERE vil_no = {0}'.format(no))
        db_password = c.fetchone()[0]
        if db_password is not None:
            return db_password
        else:
            return ''
