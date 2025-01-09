from datetime import datetime

from rest_framework.exceptions import ValidationError



class PostNameValidator:


    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        forbiden_words = ["ерунда", "глупость", "чепуха"]
        name = value.get(self.field)
        res = 0
        for el in name.split(" "):
            if el and el.lower() in forbiden_words:
                res = 1
                break
        if res == 1:
            raise ValidationError(
                "использованы запрещенные слова (ерунда, глупость, чепуха)"
            )

