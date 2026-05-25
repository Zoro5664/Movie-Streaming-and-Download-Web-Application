import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,AbstractUser
import datetime

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(
#             email=email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class MyUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Images/', filename)

def vfilepath(instance, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s%s" % (timeNow, instance.name, ".mp4")
    return os.path.join(filename)

class m_details(models.Model):
    name = models.TextField(max_length=191)
    description = models.TextField(max_length=500, null=True)
    tlink = models.TextField(max_length=500,null=True)
    mlink = models.FileField(upload_to=vfilepath, null=True, blank=True)
    category = models.TextField(max_length=50)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)


