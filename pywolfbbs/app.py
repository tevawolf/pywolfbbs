from datetime import timedelta

from flask import Flask

from pywolfbbs.application.view.VilMemberJoinView import VilMemberJoinView
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
from pywolfbbs.application.view._develop_._DevViews_ import _DevProgressDateView_, _DevProgressEpilogueView_, \
    _DevProgressEndView_


def create_app():

    app = Flask(__name__, static_folder="presentation/static", template_folder="presentation/templates")
    app.config.from_object('pywolfbbs.config.Config')
    app.permanent_session_lifetime = timedelta(minutes=30)

    app.add_url_rule('/', view_func=InitView.as_view('init'))
    app.add_url_rule('/vil/<int:no>/<int:disp_date>/', view_func=GameVilView.as_view('vil'))
    app.add_url_rule('/vil/join/', view_func=VilMemberJoinView.as_view('member_join'))
    app.add_url_rule('/vil/addspeech/', view_func=AddSpeechView.as_view('speech_add'))

    app.add_url_rule('/vil/private/vil<int:no>/day<int:disp_date>/', view_func=GameVilPrivateAuthView.as_view('vil_private_auth'))
    app.add_url_rule('/vil/authprivatepath/', view_func=GameVilPrivatePasswordInputView.as_view('vil_private_password'))
    app.add_url_rule('/vil/authreadonlypath/', view_func=GameVilReadonlyPasswordInputView.as_view('vil_readonly_password'))

    app.add_url_rule('/createvil/', view_func=GameVilCreateView.as_view('create_vil'))

    app.add_url_rule('/signin/', view_func=SignInView.as_view('signin'))
    app.add_url_rule('/signout/', view_func=SignOutView.as_view('signout'))
    app.add_url_rule('/signup/', view_func=SignUpView.as_view('signup'))


    # 開発用
    app.add_url_rule('/dev_progress_date/<int:vil_no>/', view_func=_DevProgressDateView_.as_view('dev_progress_date'))
    app.add_url_rule('/dev_progress_epilogue/<int:vil_no>/', view_func=_DevProgressEpilogueView_.as_view('dev_progress_epilogue'))
    app.add_url_rule('/dev_progress_end/<int:vil_no>/', view_func=_DevProgressEndView_.as_view('dev_progress_end'))

    return app


app = create_app()
