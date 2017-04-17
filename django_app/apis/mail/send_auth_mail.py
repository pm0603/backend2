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
        pm0603에 가입해주셔서 감사합니다. 링크를 누르시면 회원가입이 완료됩니다.
        {activate_url}
        """.format(activate_url=activate_url),
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
    )
