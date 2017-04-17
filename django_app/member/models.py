from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from passlib.hash import pbkdf2_sha512

from apis.mail import send_auth_mail
from config import settings
from content_api.models import Bookmark
from content_api.models import Content


class UserManager(BaseUserManager):
    def create_userhash(self, user):
        hashed_email = pbkdf2_sha512.using(rounds=8000, salt_size=20).hash(user.email)[:40]
        UserHash.objects.create(user=user,
                                hashed_email=hashed_email + settings.SECRET_KEY)

        send_auth_mail.send_activation_mail(user_email=user.email,
                                            hashed_email=hashed_email)

    def create_user(self, email, username, password, **extra_fields):
        user = MyUser(
            email=email,
            username=username,
            **extra_fields)
        user.set_password(password)
        user.save()

        self.create_userhash(user)

        return user

    def _create_user(self, email, username, password, **extra_fields):
        user = MyUser(
            email=email,
            username=username,
            **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, username, password, **extra_fields)

    def create_facebook_user(self, email, username, facebook_id, password=None):
        user = MyUser(
            email=email,
            username=username,
            facebook_id=facebook_id)
        user.is_facebook = True
        user.is_active = True
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    joined_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    facebook_id = models.CharField(max_length=50, blank=True)
    is_facebook = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = UserManager()

    # 중간자 모델인 Bookmark를 이용해 User와 연결 - 최영민
    bookmarks = models.ManyToManyField(Content, through=Bookmark)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


class UserHash(models.Model):
    user = models.ForeignKey(MyUser)
    hashed_email = models.CharField(max_length=200)
