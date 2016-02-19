from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# User Related Model goes here

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User should have a valid email address')
        if not kwargs.get('username'):
            raise ValueError('User should have a valid username.')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()
        return account

class Account(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    firstname = models.CharField(max_length=40, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    tagline = models.CharField(max_length=150, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.firstname, self.lastname])

    def get_short_name(self):
        return self.firstname

