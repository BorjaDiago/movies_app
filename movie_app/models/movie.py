from django.db import models
from django.urls import reverse
import uuid


class Movie(models.Model):
    """
    Movie class
    """

    uuid = models.CharField(primary_key=True, default=uuid.uuid4, max_length=64, null=False, editable=False)
    title = models.CharField(max_length=30)
    characters = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    rating = models.FloatField(max_length=10)
    synopsis = models.TextField(max_length=5000)

    @property
    def movie_id(self):
        return self.id

    def __str__(self):
        """
        Return the title of the film and the director's name.
        """
        return '{0} directed by {1}'.format(self.title, self.director)

    class Meta:
        ordering = ['rating', 'title']

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('movie-detail', args=[str(self.uuid)])

