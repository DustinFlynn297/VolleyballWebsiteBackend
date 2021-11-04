import re
from django.urls import path
from leagues import views

urlpatterns = [
    path('all/', views.get_all_leagues),
    path('', views.post_leagues),
]