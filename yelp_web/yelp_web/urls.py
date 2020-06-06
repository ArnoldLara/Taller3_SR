
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('usuarios/login',views.login_view,name='login'),
    path('usuarios/logout',views.logout_view,name='logout'),
    path('usuarios/registro',views.registro,name='registro'),
    path('ratings/',include('rating.urls')),
    path('recommendations/',include('recommendation.urls')),
]
