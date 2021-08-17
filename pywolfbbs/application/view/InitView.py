from flask import render_template
from flask.views import MethodView

from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.application.service.GameFrontService import GameFrontService


class InitView(MethodView):
    """
    ゲームフロントページ初期表示View
    """

    @staticmethod
    def get():
        front = GameFrontService.initDisplay()

        return render_template('front.html',
                               vils=front.postAllGameVils(),
                               public_levels=(
                                   GameVilPublicLevel.公開,
                                   GameVilPublicLevel.入村PASS必要,
                                   GameVilPublicLevel.閲覧PASS必要,
                                   )
                               )
