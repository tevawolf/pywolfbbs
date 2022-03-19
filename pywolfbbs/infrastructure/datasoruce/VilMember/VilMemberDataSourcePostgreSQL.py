from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.VilMember.VilMemberRepository import VilMemberRepository


class VilMemberDataSourcePostgreSQL(VilMemberRepository):

    def queryVilMemberByPlayerId(self, vil_no: int, player_id: str) -> []:

        member = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute(f"""SELECT * FROM vilmembers WHERE vil_no = {vil_no} and player_id = '{player_id}' """)
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

        c.execute(f"""SELECT * FROM vilmembers WHERE vil_no = {vil_no} and member_no = '{member_no}' """)
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

        c.execute(f"""SELECT * FROM vilmembers WHERE vil_no = {vil_no}""")
        rows = c.fetchall()

        for row in rows:
            member_list.append([row[0], row[1], row[2], row[3], row[4], row[5]])

        c.close()

        return member_list

    def addMember(self, conn, vil_no: int, player_id: str, member_name: str, member_title: str) -> int:

        c = conn.cursor()

        c.execute(f"""SELECT MAX(member_no) FROM vilmembers WHERE vil_no = {vil_no}""")
        member_no = c.fetchone()[0]
        if member_no is not None:
            member_no = int(member_no) + 1
        else:
            member_no = 1

        c.execute(f"""INSERT INTO vilmembers(vil_no, player_id, member_no, member_name, member_title)
                    VALUES ({vil_no}, '{player_id}', {member_no}, '{member_name}', '{member_title}')""")

        c.close()
        return member_no

    def setHopePosition(self, conn, vil_no: int, player_id: str, position_no: int) -> bool:

        c = conn.cursor()

        c.execute(f"""UPDATE vilmembers SET hope_position = {position_no} 
                    WHERE vil_no = {vil_no} AND player_id = '{player_id}'""")

        c.close()
        return True

    def setPosition(self, conn, vil_no: int, player_id: str, position_no: int) -> bool:

        c = conn.cursor()

        c.execute(f"""UPDATE vilmembers SET position = {position_no} 
                    WHERE vil_no = {vil_no} AND player_id = '{player_id}'""")

        c.close()
        return True
