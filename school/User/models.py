from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    # is_admin = models.BooleanField(False)
    # is_teacher = models.BooleanField(False)
    # is_student = models.BooleanField(False)
    
    def create_user(self, email, name ,password = None, is_active = True):
        if not email:
            raise ValueError('User must have email address')
        if not name:
            raise ValueError('Required Field')
        user = self.model(
            email = self.normalize_email(email),
            name= name,
            password=password,
        )
    
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, password):
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
    def is_email_registered(self, email):
        user = self.filter(email=email)
        if user.count() > 0:
            return True
        return False

class Userobject(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email_address',
        unique=True
    )
    name = models.CharField(
        max_length=100, null = False, blank=False,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

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