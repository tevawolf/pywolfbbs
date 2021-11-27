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
    def get(no: int, disp_date: int):

        # 村情報を取得
        vil, dates = GameVilService.getVilDate(no)
        # 表示する発言を取得
        speeches = SpeechService.getSpeeches(no, disp_date)

        # 参加者リスト＆フィルタ機能）を取得
        members_states = VilMemberDateStateService.displayVilMemberDateStateList(no, disp_date)

        if 'player_id' in session:
            # ログイン済みの場合、プレイヤー自身の参加者情報を取得
            player_id = session['player_id']
            self_info = VilMemberService.findVilMemberByPlayerId(no, player_id)

            # 入村済みの場合
            if self_info is not None:
                # プロローグの場合は希望役職選択フォームを取得
                if vil.current_date_status == GameVilDateStatus.プロローグ:
                    # FIXME 仮にG16編成で
                    html_position_select = \
                        OrganizationService.displayHopePositionSelect(1, 16, self_info.hope_position.getValue(), no, disp_date)
                else:
                    html_position_select = None

                # 進行中の場合は投票リストと能力行使対象リストを取得
                # 自分以外の生存者のリストを取得し、選択フォーム生成
                if vil.current_date_status == GameVilDateStatus.進行中:
                    # 投票先、能力行使先などを取得
                    self_state = VilMemberDateStateService.findVilMemberDateState(no, self_info.member_no.getValue(), disp_date)

                    votes = VilMemberDateStateService.displayVoteSelect(no, disp_date, self_state.vote_member.getValue())
                    use_abilities = VilMemberDateStateService.displayUseAbilitySelect(no, disp_date, self_state.use_ability_member.getValue())
                else:
                    votes = None
                    use_abilities = None
            else:
                html_position_select = None
                votes = None
                use_abilities = None
        else:
            self_info = None
            html_position_select = None
            votes = None
            use_abilities = None

        return render_template('vil.html',
                               vil=vil,
                               dates=dates,
                               disp_date=disp_date,
                               speeches=speeches,
                               members_states=members_states,
                               self_info=self_info,
                               html_position_select=html_position_select,
                               votes=votes,
                               use_abilities=use_abilities,
                               public_level=GameVilPublicLevel,
                               date_status=GameVilDateStatus,
                               )
