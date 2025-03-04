from .sign_in import SignIn
from .send_confirm import SendConfirm
from .check_confirm import CheckConfirm
class Auth(SignIn, SendConfirm, CheckConfirm):
    pass
