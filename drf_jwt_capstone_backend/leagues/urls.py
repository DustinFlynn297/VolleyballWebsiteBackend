from django.urls import path
from leagues import views

urlpatterns = [
    path('all/', views.get_all_leagues),
    path('', views.user_leagues),
    path('<int:pk>/', views.league_detail),
]