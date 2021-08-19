from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.GameVil.GameFrontRepository import GameFrontRepository


class GameFrontDataSourcePostgreSQL(GameFrontRepository):

    def queryGameVilList(self) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM gamevils ORDER BY vil_no DESC')
        rows = c.fetchall()
        thread_list = []
        for row in rows:
            thread_list.append([row[0], row[1], row[2]])
        c.close()

        return thread_list
