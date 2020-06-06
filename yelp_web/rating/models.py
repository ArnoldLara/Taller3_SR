from django.db import models

# Create your models here.
class ratings(models.Model):
    user_id = models.CharField(max_length=50)
    movie_id = models.CharField(max_length=10)
    rating = models.DecimalField(max_digits=8, decimal_places=0, default=0.0)

    def __str__(self):
        return self.user_id

class movies(models.Model):
    movie_id = models.CharField(max_length=500)
    title = models.CharField(max_length=10)
    genre = models.CharField(max_length=300)

    def __str__(self):
        return self.title
