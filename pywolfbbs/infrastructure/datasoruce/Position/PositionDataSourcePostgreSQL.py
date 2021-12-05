import psycopg2
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.Position.PositionRepository import PositionRepository


class PositionDataSourcePostgreSQL(PositionRepository):

    def queryPositionById(self, position_no: int) -> []:

        position = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM positions WHERE position_no = {0} """.format(position_no))
        fetch = c.fetchone()

        if fetch is not None:
            position.append(fetch[1])  # position_name
            position.append(fetch[2])  # description
            position.append(fetch[3])  # ability_name
            position.append(fetch[4])  # camp_no

        c.close()

        return position

