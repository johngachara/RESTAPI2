from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(unique=True,max_length=17)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.DateField()
    artists = models.ManyToManyField(Artist,related_name='artists')
    def __str__(self):
        return self.title


class Songs(models.Model):
    track_name = models.CharField(max_length=50)
    duration = models.IntegerField()
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name='songs')

    def __str__(self):
        return self.track_name

