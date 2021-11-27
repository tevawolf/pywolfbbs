from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.VilMember.VilMemberRepository import VilMemberRepository


class VilMemberDataSourcePostgreSQL(VilMemberRepository):

    def queryVilMemberByPlayerId(self, vil_no: int, player_id: str) -> []:

        member = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM vilmembers WHERE vil_no = {0} and player_id = '{1}' """.format(vil_no, player_id))
        fetch = c.fetchone()

        if fetch is not None:
            member.append(fetch[2])  # member_no
            member.append(fetch[3])  # member_name
            member.append(fetch[4])  # member_title
            member.append(fetch[5])  # hope_position
            member.append(fetch[6])  # position

        c.close()

        return member

    def queryVilMemberByMemberNo(self, vil_no: int, member_no: int) -> []:

        member = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM vilmembers WHERE vil_no = {0} and member_no = '{1}' """.format(vil_no, member_no))
        fetch = c.fetchone()

        if fetch is not None:
            member.append(fetch[1])  # player_id
            member.append(fetch[3])  # member_name
            member.append(fetch[4])  # member_title
            member.append(fetch[5])  # hope_position
            member.append(fetch[6])  # position

        c.close()

        return member

    def queryVilMemberList(self, vil_no: int) -> []:

        member_list = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM vilmembers WHERE vil_no = {0}""".format(vil_no))
        rows = c.fetchall()

        for row in rows:
            member_list.append([row[0], row[1], row[2], row[3], row[4], row[5]])

        c.close()

        return member_list

    def addMember(self, vil_no: int, player_id: str, member_name: str, member_title: str) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(member_no) FROM vilmembers WHERE vil_no = {0}""".format(vil_no))
        no = c.fetchone()[0]
        if no is not None:
            no = no + 1
        else:
            no = 1

        c.execute("""INSERT INTO vilmembers(vil_no, player_id, member_no, member_name, member_title)
                    VALUES ({0}, '{1}', {2}, '{3}', '{4}')""".format(vil_no, player_id, no, member_name, member_title))
        conn.commit()

        c.close()
        return True

    def setHopePosition(self, vil_no: int, player_id: str, position_no: int) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""UPDATE vilmembers SET hope_position = {0} WHERE vil_no = {1} AND player_id = '{2}'"""
                  .format(position_no, vil_no, player_id))
        conn.commit()

        c.close()
        return True
