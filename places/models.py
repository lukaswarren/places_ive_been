from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Place(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    date = models.DateField()
    visit_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Picture(models.Model):
    picture_id = models.CharField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
