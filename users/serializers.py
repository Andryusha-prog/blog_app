from rest_framework.serializers import ModelSerializer

from users.models import User
from users.validators import EmailCustomValidator, PasswordCustomValidator


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        validators = [EmailCustomValidator(field="email"), PasswordCustomValidator(field="password")]
