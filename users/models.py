from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address',unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    is_verified = models.BooleanField(default=False)
    number = models.IntegerField(default=000000000000)
    phone = models.BigIntegerField(default=0000000000000 )

class Profile(models.Model):
    about_me = models.TextField()
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.TextField(default='N/A')
    number = models.IntegerField(default=000000000000)
    phone = models.IntegerField(default=0000000000000)


    def __str__(self):
        return self.user.username

class workers(models.Model):
    email = models.EmailField(max_length=100)





