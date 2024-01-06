from django.views import generic
from django.shortcuts import render
from .models import Movies
from .forms import SearchForm

app = "films"

class MoviesListView(generic.ListView):
    model = Movies
    template_name = f"{app}/index.html"
    context_object_name = 'movies'
    queryset = Movies.objects.order_by('title')[:12]
    def get_queryset(self):
        # Obtén el parámetro de la URL para determinar qué lista mostrar
        list_type = self.request.GET.get('list_type', 'top_movies')
        
        if list_type == 'full_movies':
            # Mostrar la lista completa de películas
            return Movies.objects.all().order_by('title')
        elif list_type == "dvd_movies":
            return Movies.objects.filter(type_film="DVD").order_by('title')
        elif list_type == "blue_ray_movies":
            return Movies.objects.filter(type_film="Blu-ray").order_by('title')
        else:
            # Mostrar la lista superior de películas
            return Movies.objects.order_by('title')[:12]
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_list_type'] = self.request.GET.get('list_type', 'top_movies')
        return context

class MovieDetailView(generic.DetailView):
    model = Movies
    template_name = f"{app}/movie_detail.html"
    context_object_name = 'detail'

class SearchView(generic.ListView):
    model = Movies
    template_name = f"{app}/index.html"
    context_object_name = 'all_search_results'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        result_query = Movies.objects.filter(title__icontains=query).order_by('title')
        if result_query:
            return result_query
        else:
            return Movies.objects.none()
            