from django.urls import path
from leagues import views

urlpatterns = [
    # path('all/', views.get_all_leagues),
    path('user/', views.user_leagues),
    path('delete/<int:pk>', views.delete_league),
    path('<pk>', views.league_detail),
    path('edit/<pk>', views.update_league_detail),

    
]