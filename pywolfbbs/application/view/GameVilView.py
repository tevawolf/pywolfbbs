from flask import render_template, session
from flask.views import MethodView

from pywolfbbs.application.service.OrganizationService import OrganizationService
from pywolfbbs.application.service.SpeechService import SpeechService
from pywolfbbs.application.service.VilMemberDateStateService import VilMemberDateStateService
from pywolfbbs.application.service.VilMemberService import VilMemberService
from pywolfbbs.domain.GameVil.enum.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.enum.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.application.service.GameVilService import GameVilService


class GameVilView(MethodView):

    @staticmethod
    def get(vil_no: int, disp_date: int):

        # 村情報を取得
        vil, dates = GameVilService.getVilDate(vil_no)
        # 表示する発言を取得
        speeches = SpeechService.getSpeeches(vil_no, disp_date)

        # 参加者リスト＆フィルタ機能）を取得
        members_states = VilMemberDateStateService.displayVilMemberDateStateList(vil_no, disp_date)

        if 'player_id' in session:
            # ログイン済みの場合、プレイヤー自身の参加者情報を取得
            player_id = session['player_id']
            self_info = VilMemberService.findVilMemberByPlayerId(vil_no, player_id)

            # 入村済みの場合
            if self_info is not None:
                # プロローグの場合は希望役職選択フォームを取得
                if vil.current_date_status == GameVilDateStatus.プロローグ:
                    # FIXME 仮にG16編成で
                    html_position_select = \
                        OrganizationService.displayHopePositionSelect(1, 16, self_info.hope_position.getValue(), vil_no, disp_date)
                else:
                    html_position_select = None

                # 進行中の場合
                if vil.current_date_status == GameVilDateStatus.進行中:
                    # 投票先、能力行使先などを取得
                    self_state = VilMemberDateStateService.findVilMemberDateState(vil_no, self_info.member_no.getValue(), disp_date)
                    # 投票セットフォームと能力行使対象セットフォームを取得
                    # 自分以外の生存者のリストを取得し、選択フォーム生成
                    html_vote_select = VilMemberDateStateService.displayVoteSelect(vil_no, disp_date, self_state.vote_member.getValue())
                    html_use_ability_select = \
                        VilMemberDateStateService.displayUseAbilitySelect(
                            vil_no, disp_date, self_state.use_ability_member.getValue(), self_info.position.getValue())
                    # 役職説明欄を取得
                    position_description = VilMemberService.displayPositionDescription(vil_no, player_id)

                else:
                    html_vote_select = None
                    html_use_ability_select = None
                    position_description = None
            else:
                html_position_select = None
                html_vote_select = None
                html_use_ability_select = None
                position_description = None
        else:
            self_info = None
            html_position_select = None
            html_vote_select = None
            html_use_ability_select = None
            position_description = None

        return render_template('vil.html',
                               vil=vil,
                               dates=dates,
                               disp_date=disp_date,
                               speeches=speeches,
                               members_states=members_states,
                               self_info=self_info,
                               html_position_select=html_position_select,
                               html_vote_select=html_vote_select,
                               html_use_ability_select=html_use_ability_select,
                               public_level=GameVilPublicLevel,
                               date_status=GameVilDateStatus,
                               position_description=position_description,
                               )
