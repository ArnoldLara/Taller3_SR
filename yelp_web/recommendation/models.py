from django.db import models

# Create your models here.
# Create your models here.
class svd_db(models.Model):
    user_id = models.CharField(max_length=50)
    movie_id = models.CharField(max_length=10)
    rating = models.DecimalField(max_digits=8, decimal_places=0, default=0.0)

    def __str__(self):
        return self.user_id

class neo4j_db(models.Model):
    from_movie = models.CharField(max_length=50)
    movie_name = models.CharField(max_length=10)
    similarity = models.DecimalField(max_digits=8, decimal_places=0, default=0.0)

    def __str__(self):
        return self.movie_name
