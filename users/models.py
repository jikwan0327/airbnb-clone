from operator import mod
from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser): #유저기능 확장

    """Custom User Model"""

    GENDER_MALE ="male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other "),
    ) 

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "KO "),
        (LANGUAGE_ENGLISH, "EN")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10, blank=True ) #CharField에는 인자 하나가 필수임, CharField는 한줄 텍스트

    bio = models.TextField(blank=True) #필드 #텍스트 필드는 여러줄 텍스트
    #blank는 required를 없애줌(필수 입력이 아니게 바꿈)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=6, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False) 