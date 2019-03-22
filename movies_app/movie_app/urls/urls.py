
from django.conf.urls import url

from movie_app import views as movie_app_views

urlpatterns = [
    url(r'^$', movie_app_views.index_view.get, name='index_view'),
    url(r'^movie/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', movie_app_views.MovieDetailView.as_view(), name='movie-detail'),
]
