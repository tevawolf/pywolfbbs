from flask import render_template, session, url_for
from flask.views import MethodView
from werkzeug.utils import redirect


class GameVilPrivateAuthView(MethodView):

    @staticmethod
    def get(no: int):
        if 'vil_auth' in session:
            if session['vil_auth'] and session['vil_auth_no'] == no:
                return redirect(url_for('vil', no=no))

        return render_template('vil_private_auth.html', no=no)

