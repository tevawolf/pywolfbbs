from flask import render_template
from flask.views import MethodView

from pywolfbbs.domain.GameVil.object.GameVilDateStatus import GameVilDateStatus
from pywolfbbs.domain.GameVil.object.GameVilPublicLevel import GameVilPublicLevel
from pywolfbbs.application.service.GameVilService import GameVilService


class GameVilView(MethodView):

    @staticmethod
    def get(no: int, disp_date: int):
        vil = GameVilService.displayVil(no, disp_date)

        return render_template('vil.html', vil=vil, disp_date=disp_date,
                               PUBLIC_LEVEL_READONLY=GameVilPublicLevel.入村PASS必要,
                               CUR_DATE_STATUS_PROLOGUE=GameVilDateStatus.プロローグ,
                               CUR_DATE_STATUS_PROGRESS=GameVilDateStatus.進行中,
                               CUR_DATE_STATUS_EPILOGUE=GameVilDateStatus.エピローグ,
                               CUR_DATE_STATUS_END=GameVilDateStatus.終了,
                               )
