from django.urls import path

from . import views

urlpatterns = [
    path('svd',views.svdRecommendation,name='svd_rec'),
    path('neo4j',views.neo4jRecommendation,name='neo4j_rec'),
]
