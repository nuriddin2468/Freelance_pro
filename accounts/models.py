from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class EmployerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    COMPANY_SIZE = (
        ('small', "2-9 Employees"),
        ('medium', "10-99 Employees"),
        ('big', "100-499 Employees"),
        ('very big', "More than 500 Employees")
    )
    user = models.OneToOneField(User, related_name='companies' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    banner = models.ImageField(upload_to="company/banner/")
    bannerMini = models.ImageField(upload_to='company/banner/mini/', default='')
    logo = models.ImageField(upload_to="company/logo/")
    about = models.TextField(max_length=1024)
    employees = models.CharField(max_length=20, choices=COMPANY_SIZE, default='medium')
    verified = models.BooleanField(default=False)
    social_twitter = models.CharField(default=None, max_length=240)
    social_facebook = models.CharField(default=None, max_length=240)
    social_linkedin = models.CharField(default=None, max_length=240)

    def __str__(self):
        return self.name
