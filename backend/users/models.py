from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, firstName=None, lastName=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstName=firstName,
            lastName=lastName,
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password=None, firstName=None, lastName=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
            firstName=firstName,
            lastName=lastName,
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
    

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    firstName = models.CharField(max_length=30, blank=True, null=True)
    lastName = models.CharField(max_length=30, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return f"{self.firstName} {self.lastName}" if self.firstName and self.lastName else self.username

    def get_short_name(self):
        return self.username    
    objects = CustomUserManager()

    
# Create your models here.
