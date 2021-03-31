from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User


class UserProfileManager(BaseUserManager):
    '''Manager for user profiles'''
    def create_user(self, name, email, password=None, **extra_fields):
        '''create a new user'''
        if not email:
            raise ValueError("Email is a required field")

        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None, **extra_fields):
        '''create a new user'''
        if not email:
            raise ValueError("Email is a required field")

        email = self.normalize_email(email)
        user = self.create_user(name=name, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"Database user model  for users in in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retrieve full name of the user'''
        return self.name

    def get_short_name(self):
        '''Retrieve short name of the user'''
        return self.name

    def __str__(self):
        '''Return string representation of user'''
        return self.email
