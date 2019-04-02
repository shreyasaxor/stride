from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Expery(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_date = models.DateTimeField()