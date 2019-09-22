from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CompanyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    banner = models.ImageField(upload_to="company/banner/")
    bannerMini = models.ImageField(upload_to='company/banner/mini/' , default='')
    logo = models.ImageField(upload_to="company/logo/")
    about = models.CharField(max_length=240)
    verified = models.BooleanField(default=False)
    social_twitter = models.CharField(default=None, max_length=240)
    social_facebook = models.CharField(default=None, max_length=240)
    social_linkedin = models.CharField(default=None, max_length=240)

    def __str__(self):
        return self.name
