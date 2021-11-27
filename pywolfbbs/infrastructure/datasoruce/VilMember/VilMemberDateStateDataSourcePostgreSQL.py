from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.VilMember.VilMemberDateStateRepository import VilMemberDateStateRepository


class VilMemberDateStateDataSourcePostgreSQL(VilMemberDateStateRepository):

    def queryVilMemberDateState(self, vil_no: int, member_no: int, date: int):

        state = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM vilmember_date_states 
        WHERE vil_no = {0} AND member_no = '{1}' AND date_num = {2}""".format(vil_no, member_no, date))
        fetch = c.fetchone()

        if fetch is not None:
            state.append(fetch[3])  # remain_speech_num
            state.append(fetch[4])  # remain_speech_pt
            state.append(fetch[5])  # vote_member
            state.append(fetch[6])  # use_ability_member

        c.close()

        return state

    def queryVilMemberDateStateList(self, vil_no: int, member_no: str) -> []:

        state = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM vilmember_date_states WHERE vil_no = {0} and member_no = '{1}' """.format(vil_no, member_no))
        fetch = c.fetchall()

        for f in fetch:
            state.append([f[2], f[3], f[4], f[5], f[6]])

        c.close()

        return state

    def queryVilMemberDateStateDateList(self, vil_no: int, date: int):
        state = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT * FROM vilmember_date_states WHERE vil_no = {0} and date_num = '{1}' """.format(vil_no, date))
        fetch = c.fetchall()

        for f in fetch:
            state.append([f[1], f[3], f[4], f[5], f[6]])

        c.close()

        return state

    def addMemberDateState(self, vil_no: int, member_no: int, date: int):
        pass