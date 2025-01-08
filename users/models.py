from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.CharField(unique=True, max_length=50, verbose_name='email')
    phone = PhoneNumberField(blank=True, null=True, verbose_name='номер телефона')
    birth_date = models.DateField(verbose_name='дата рождения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
