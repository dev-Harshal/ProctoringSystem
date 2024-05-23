from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10,null=True,blank=True,choices=(('Teacher','Teacher'),('Student','Student')),default="Student")
    photo = models.ImageField(upload_to="UsersImages/")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class OTP(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.CharField(max_length=4)