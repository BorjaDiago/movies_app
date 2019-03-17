from django.db import models
from django.urls import reverse


class Director(models.Model):
    """
    Director class
    """
    director_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        """
        Return the director's name.
        """
        return '{0}'.format(self.name)

    class Meta:
        db_table = 'director'
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('director-detail', args=[str(self.director_id)])
