from flask import render_template
from flask.views import MethodView

from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.application.service.GameVilService import GameVilService


class GameVilView(MethodView):

    @staticmethod
    def get(no: int):
        vil = GameVilService.displayVil(no)

        return render_template('vil.html', vil=vil, PUBLIC_LEVEL_READONLY=GameVilPublicLevel.入村PASS必要)
