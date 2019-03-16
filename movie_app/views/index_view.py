from django.shortcuts import render

from movie_app.services.movie_services import MovieServices


def get(request):
    all_movies = MovieServices.get_all_movies()

    return render(request, 'index.html', context={
        'all_movies': all_movies,
        'count': all_movies.count(),
        'request': request,
        }, )
