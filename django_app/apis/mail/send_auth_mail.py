from django.core.mail import send_mail

from config import settings

__all__ = [
    'send_activation_mail',
]


def send_activation_mail(user_email, hashed_email):
    hashed_email = hashed_email.replace("$pbkdf2-sha512$8000$", "")
    activate_url = "http://127.0.0.1:8000/user/activate/{hashed_email}/".format(hashed_email=hashed_email)
    send_mail(
        "pm0603 Signup mail",
        """
        ♚♚p☆m☆0☆6☆0☆3♚♚가입시$$전원 카드팩☜☜뒷면100%증정※ ♜공연☆전시정보♜ 무료증정￥ 특정조건 §§북마크3§§★예약서비스★획득기회@@@ 즉시이동
        {activate_url}
        """.format(activate_url=activate_url),
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
    )
