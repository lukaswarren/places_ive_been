from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class Place(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latLng = models.CharField(max_length=50)
    visible = models.BooleanField(default=False)
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return f"{self.city}, {self.country}"


class Visit(models.Model):
    place = models.ForeignKey(Place, related_name='visits', on_delete=models.CASCADE)
    date = models.DateField()
    visitNumber = models.PositiveIntegerField()
    author = models.CharField(max_length=100, blank=True, null=True)  # Optional author field
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author} on {self.date}" if self.title and self.author else "Visit on {}".format(
            self.date)


class Image(models.Model):
    visit = models.ForeignKey(Visit, related_name='images', on_delete=models.CASCADE)
    imgID = models.CharField(max_length=255)  # Unique identifier for the image

    def __str__(self):
        return self.imgID
