from .sign_in import SignIn
from .send_confirm import SendConfirm
class Auth(SignIn, SendConfirm):
    pass
