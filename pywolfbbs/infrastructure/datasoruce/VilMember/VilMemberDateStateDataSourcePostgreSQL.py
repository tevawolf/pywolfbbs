from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.VilMember.VilMemberDateStateRepository import VilMemberDateStateRepository


class VilMemberDateStateDataSourcePostgreSQL(VilMemberDateStateRepository):

    def queryVilMemberDateState(self, vil_no: int, member_no: int, date: int):

        state = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute(f"""SELECT * FROM vilmember_date_states 
        WHERE vil_no = {vil_no} AND member_no = '{member_no}' AND date_num = {date}""")
        fetch = c.fetchone()

        if fetch is not None:
            state.append(fetch[3])  # remain_speech_num
            state.append(fetch[4])  # remain_speech_pt
            state.append(fetch[5])  # vote_member
            state.append(fetch[6])  # use_ability_member
            state.append(fetch[7])  # place

        c.close()

        return state

    def queryVilMemberDateStateList(self, vil_no: int, member_no: str) -> []:

        state = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute(f"""SELECT * FROM vilmember_date_states WHERE vil_no = {vil_no} and member_no = '{member_no}' """)
        fetch = c.fetchall()

        for f in fetch:
            state.append([f[2], f[3], f[4], f[5], f[6], f[7]])

        c.close()

        return state

    def queryVilMemberDateStateDateList(self, vil_no: int, date: int):
        state = []

        conn = get_postgres()
        c = conn.cursor()

        c.execute(f"""SELECT * FROM vilmember_date_states WHERE vil_no = {vil_no} and date_num = '{date}' """)
        fetch = c.fetchall()

        for f in fetch:
            state.append([f[1], f[3], f[4], f[5], f[6], f[7]])

        c.close()

        return state

    def addMemberDateState(self, conn, vil_no: int, member_no: int, date: int, speech_num: int, pt: int, vote: int,
                           use: int, place: int) -> bool:

        c = conn.cursor()

        c.execute(f"""INSERT INTO vilmember_date_states(vil_no, member_no, date_num, remain_speech_num,
                    remain_speech_pt, vote_member, use_ability_member, place)
                    VALUES ({vil_no}, '{member_no}', {date}, '{speech_num}', 
                    '{pt}', '{vote}', '{use}', '{place}')""")

        c.close()
        return True

    def updateVote(self, conn, vil_no: int, member_no: int, date: int, vote: int):

        c = conn.cursor()

        c.execute(f"""UPDATE vilmember_date_states SET vote_member = {vote} 
                    WHERE vil_no = {vil_no} AND member_no = {member_no} AND date_num = {date}""")

        c.close()
        return True

    def updateUseAbility(self, conn, vil_no: int, member_no: int, date: int, use_ability: int):

        c = conn.cursor()

        c.execute(f"""UPDATE vilmember_date_states SET use_ability_member = {use_ability} 
                    WHERE vil_no = {vil_no} AND member_no = {member_no} AND date_num = {date}""")

        c.close()
        return True

    def updateRemainSpeechNumber(self, conn, vil_no: int, member_no: int, date: int, remain_number: int):

        c = conn.cursor()

        c.execute(f"""UPDATE vilmember_date_states SET remain_speech_num = {remain_number} 
                    WHERE vil_no = {vil_no} AND member_no = {member_no} AND date_num = {date}""")

        c.close()
        return True
