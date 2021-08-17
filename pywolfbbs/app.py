from datetime import timedelta

from flask import Flask

from pywolfbbs.application.view.AddSpeechView import AddSpeechView
from pywolfbbs.application.view.InitView import InitView
from pywolfbbs.application.view.SignInView import SignInView
from pywolfbbs.application.view.SignOutView import SignOutView
from pywolfbbs.application.view.SignUpView import SignUpView
from pywolfbbs.application.view.GameVilCreateView import GameVilCreateView
from pywolfbbs.application.view.GameVilPrivateAuthView import GameVilPrivateAuthView
from pywolfbbs.application.view.GameVilPrivatePasswordInputView import GameVilPrivatePasswordInputView
from pywolfbbs.application.view.GameVilReadonlyPasswordInputView import GameVilReadonlyPasswordInputView
from pywolfbbs.application.view.GameVilView import GameVilView


def create_app():

    app = Flask(__name__, static_folder="presentation/static", template_folder="presentation/templates")
    app.config.from_object('pywolfbbs.config.Config')
    app.permanent_session_lifetime = timedelta(minutes=30)

    app.add_url_rule('/', view_func=InitView.as_view('init'))
    app.add_url_rule('/vil/addspeech/', view_func=AddSpeechView.as_view('speech_add'))
    app.add_url_rule('/vil/<int:no>/', view_func=GameVilView.as_view('vil'))

    app.add_url_rule('/vil/private/<int:no>/', view_func=GameVilPrivateAuthView.as_view('vil_private_auth'))
    app.add_url_rule('/vil/authprivatepath/', view_func=GameVilPrivatePasswordInputView.as_view('vil_private_password'))
    app.add_url_rule('/vil/authreadonlypath/', view_func=GameVilReadonlyPasswordInputView.as_view('vil_readonly_password'))

    app.add_url_rule('/createvil/', view_func=GameVilCreateView.as_view('create_vil'))

    app.add_url_rule('/signin/', view_func=SignInView.as_view('signin'))
    app.add_url_rule('/signout/', view_func=SignOutView.as_view('signout'))
    app.add_url_rule('/signup/', view_func=SignUpView.as_view('signup'))

    return app


app = create_app()
