from django.urls import path

from . import views

app_name = "films"
urlpatterns = [
    path("", views.MoviesListView.as_view(), name="movies_list"),
    path("search/", views.SearchView.as_view(), name="search_list"),
    path('<uuid:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
]