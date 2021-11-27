import psycopg2
from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.Player.PlayerRepository import PlayerRepository


class PlayerDataSourcePostgreSQL(PlayerRepository):

    def addPlayer(self, player_id: str, name: str, password: bytes, tag: bytes, nonce: bytes) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()
        c.execute(r"INSERT INTO players(player_id, player_name, password, tag, nonce) VALUES " \
                      "('{0}', '{1}'".format(player_id, name) + ", %s, %s, %s )",
                  (psycopg2.Binary(password), psycopg2.Binary(tag), psycopg2.Binary(nonce),)
                  )
        conn.commit()

        c.close()
        return True

    def queryPlayer(self, player_id: str) -> []:

        player = []

        conn = get_postgres()
        c = conn.cursor()
        c.execute("SELECT * FROM players WHERE player_id = '{0}'".format(player_id))
        row = c.fetchone()

        if row is not None:
            player.append(row[0])
            player.append(row[1])
            player.append(row[2])
            player.append(row[3])
            player.append(row[4])

        c.close()

        return player
