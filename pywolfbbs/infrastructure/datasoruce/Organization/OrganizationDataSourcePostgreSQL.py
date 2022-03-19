from pywolfbbs.infrastructure.datasoruce.postgresql_db import get_postgres
from pywolfbbs.infrastructure.repository.Organization.OrganizationRepository import OrganizationRepository


class OrganizationDataSourcePostgreSQL(OrganizationRepository):

    def queryOrganizationPositionTotalList(self, organization_no: int, nop: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute(
            """
            SELECT 
                op.position_no,
                op.total
            FROM organization_positions op
            WHERE op.organization_no = {0} AND op.number_of_people = {1} AND not op.position_no = 0
            """.format(organization_no, nop)
        )
        rows = c.fetchall()
        position_list = []
        for row in rows:
            position_list.append([row[0], row[1]])
        c.close()

        return position_list

    def queryOrganizationPositionNameList(self, organization_no: int, nop: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute(
            """
            SELECT 
                p.position_no,
                p.position_name
            FROM organization_positions op
            INNER JOIN positions p
            ON op.position_no = p.position_no
            WHERE op.organization_no = {0} AND op.number_of_people = {1} AND not p.position_no = 0
            """.format(organization_no, nop)
        )
        rows = c.fetchall()
        position_list = []
        for row in rows:
            position_list.append([row[0], row[1]])
        c.close()

        return position_list
