from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name = 'home'),
    path('list/',views.list_game , name = 'list_game'),
    ]