from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
   path('', views.Home.as_view(), name='home'),
   path('profiles/', views.ProfileList.as_view(), name='profile_list'),
   path('profile/create/', views.ProfileCreate.as_view(), name='create_profile'),
   path('watch/<str:profile_id>/', views.Watch.as_view(), name='watch'),
   path('movie/details/<str:movie_id>/', views.ShowMovieDetail.as_view(), name='movie_detail'),
   path('movie/play/<str:movie_id>/', views.ShowMovie.as_view(), name='movie_play'),
]
