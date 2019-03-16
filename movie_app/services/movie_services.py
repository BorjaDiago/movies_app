from django.http import Http404

from movie_app.models import Movie


class MovieServices(object):
    @staticmethod
    def get_movie(uuid):
        try:
            return Movie.objects.get(uuid=uuid)
        except Movie.DoesNotExist:
            raise Http404

    @staticmethod
    def get_all_movies():
        try:
            return Movie.objects.all()
        except Movie.DoesNotExist:
            raise Http404
