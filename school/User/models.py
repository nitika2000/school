from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    # is_admin = models.BooleanField(False)
    # is_teacher = models.BooleanField(False)
    # is_student = models.BooleanField(False)

    def create_user(self, email, password = None, is_active = True):
        if not email:
            raise ValueError('User must have email address')
        user = self.model(
            email= self.normalize_email(email)
        )
        user.set_password = password
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class Userobject(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email_address',
        unique=True
    )
    is_active = models.BooleanField(True)
    is_admin = models.BooleanField(False)

    USERNAME_FIELD = 'email'

    object = UserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return True

    @property
    def is_staff(self):
        return self.is_admin