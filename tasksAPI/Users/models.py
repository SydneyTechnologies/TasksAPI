from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from . managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


# creating a custom user class and setting the default username to the email field for authentication
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # must have fields while inheriting from the AbstractUserClass
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # setting up the default manager
    objects = CustomUserManager()

    # set the email field to be the username
    USERNAME_FIELD = 'email'

    # must have permission functions
    def has_perm(self, obj=None):
        # does this user have permissions for this object
        return obj.owner == self
    
    def has_module_perms(self, app_label=None):
        # I really have no use case for this 
        return True
    
    def __str__(self):
        return self.email
