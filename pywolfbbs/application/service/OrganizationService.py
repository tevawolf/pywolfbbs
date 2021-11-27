from flask import url_for

from pywolfbbs.domain.Organization.factory.OrganizationFactory import OrganizationFactory


class OrganizationService:
    """
    役職編成のサービスオブジェクト
    """
    @staticmethod
    def displayAllPositionOrganization():
        """
        全編成リストを画面出力
        :return:
        """
        pass

    @staticmethod
    def displayHopePositionSelect(organization_no: int, nop: int, hope: int, vil_no: int, vil_date: int) -> str:
        """
        役職希望選択リストを画面出力
        :param organization_no:
        :param nop:
        :param hope:
        :param vil_no
        :param vil_date
        :return:
        """

        organization = OrganizationFactory.create(organization_no, '', [])
        position_list = organization.getHopePositionSelect(nop)

        html_select = '<label>希望役職</label> \
                        <form action="' + url_for('hope_position') + '" method=post class=""> \
                        <select name="hope_position">'

        for position in position_list:
            if int(position[0]) == hope:
                html_select += '<option value="{0}" selected>{1}(セット済み）</option>'.format(position[0], position[1])
            else:
                html_select += '<option value="{0}">{1}</option>'.format(position[0], position[1])

        html_select += '</select> \
                        <button type="submit" class="btn btn-danger">設定</button><br> \
                        <input type="hidden" name="vil_no" value="{0}"> \
                        <input type="hidden" name="vil_date" value="{1}"> \
                        </form>'.format(vil_no, vil_date)

        return html_select
