from django.contrib import admin
from .models import svd_db, neo4j_db

# Register your models here.
admin.site.register(svd_db)
admin.site.register(neo4j_db)
