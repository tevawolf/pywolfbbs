from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.GameVil.GameVilDateRepository import GameVilDateRepository


class GameVilDateDataSourcePostgreSQL(GameVilDateRepository):

    def queryGameVilDateList(self, vil_no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM gamevil_dates WHERE vil_no = {0} ORDER BY date_num ASC'.format(vil_no))
        rows = c.fetchall()
        date_list = []
        for row in rows:
            date_list.append([row[0], row[1], row[2]])
        c.close()

        return date_list

    def createGameVilDate(self, date: int, vil_no: int, status: int) -> bool:

        conn = get_postgres()
        c = conn.cursor()

        # プロローグの日付を追加
        c.execute("""INSERT INTO gamevil_dates(date_num, vil_no, date_status)
                    VALUES ({0}, {1}, {2})""".format(date, vil_no, status))
        conn.commit()

        c.close()
        return True
