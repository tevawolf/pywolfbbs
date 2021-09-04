from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.VilMember.VilMemberRepository import VilMemberRepository


class VilMemberDataSourcePostgreSQL(VilMemberRepository):

    def queryVilMember(self, vil_no: int, player_id: str):

        member = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM vilmembers WHERE vil_no = {0} and player_id = '{1}' """.format(vil_no, player_id))
        fetch = c.fetchone()

        if not (fetch is None):
            member.append(fetch[2])  # member_no
            member.append(fetch[3])  # member_name
            member.append(fetch[4])  # member_title

        c.close()

        return member

    def addMember(self, vil_no: int, player_id: str, member_name: str, member_title: str):

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(member_no) FROM vilmembers WHERE vil_no = {0}""".format(vil_no))
        no = c.fetchone()[0]
        if not (no is None):
            no = no + 1
        else:
            no = 1

        c.execute("""INSERT INTO vilmembers(vil_no, player_id, member_no, member_name, member_title)
                    VALUES ({0}, '{1}', {2}, '{3}', '{4}')""".format(vil_no, player_id, no, member_name, member_title))
        conn.commit()

        c.close()
        return True