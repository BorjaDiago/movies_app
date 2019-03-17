from django.shortcuts import render
from django.views import View

from movie_app.models import Character
from movie_app.services.movie_services import MovieServices


class MovieDetailView(View):
    @staticmethod
    def get(request, uuid):
        movie = MovieServices.get_movie(uuid)
        director = movie.director.all()
        characters = movie.characters.all()
        rating = movie.rating
        synopsis = movie.synopsis
        template_name = 'movie_detail.html'
        return render(request, template_name, context={
            'movie': movie,
            'director': director,
            'characters': characters,
            'rating': rating,
            'synopsis': synopsis,
        })
