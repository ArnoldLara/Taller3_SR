from django.contrib import admin
from .models import movies,ratings

# Register your models here.
admin.site.register(movies)
admin.site.register(ratings)
