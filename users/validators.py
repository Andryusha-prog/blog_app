import re

from rest_framework.exceptions import ValidationError


class EmailCustomValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        email = value.get(self.field)
        if email and not (email.endswith("mail.ru") or email.endswith("yandex.ru")):
            raise ValidationError(
                "разрешена только почты: mail.ru, yandex.ru"
            )

class PasswordCustomValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        passw = value.get(self.field)
        reg_exp_passw = re.compile('\w+[0-9]\w+')
        if passw and len(passw) < 8:
            raise ValidationError(
                "Длина пароля должна быть больше 8 символов"
            )
        if passw and not bool(reg_exp_passw.match(passw)):
            raise ValidationError(
                "Должна быть хотя бы одна цифра"
            )