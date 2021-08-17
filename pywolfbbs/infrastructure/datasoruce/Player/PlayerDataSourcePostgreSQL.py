import psycopg2
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.Player.PlayerRepository import PlayerRepository


class PlayerDataSourcePostgreSQL(PlayerRepository):

    def addPlayer(self, id: str, name: str, password: bytes, tag: bytes, nonce: bytes) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()
        c.execute(r"INSERT INTO posters(poster_id, poster_name, password, tag, nonce) VALUES " \
                      "('{0}', '{1}'".format(id, name) + ", %s, %s, %s )",
                  (psycopg2.Binary(password), psycopg2.Binary(tag), psycopg2.Binary(nonce),)
                  )
        conn.commit()

        c.close()
        return True

    def queryPlayer(self, poster_id: str) -> []:

        player = []

        conn = get_postgres()
        c = conn.cursor()
        c.execute("SELECT * FROM posters WHERE poster_id = '{0}'".format(poster_id))
        row = c.fetchone()

        if not (row is None):
            player.append(row[0])
            player.append(row[1])
            player.append(row[2])
            player.append(row[3])
            player.append(row[4])
            c.close()

        return player
