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

    @staticmethod
    def get_characters_from_movie(movie):
        try:
            return movie.characters.all()
        except Exception as ex:
            return None

    @staticmethod
    def get_directors_from_movie(movie):
        try:
            return movie.director.all()
        except Exception as ex:
            return None
