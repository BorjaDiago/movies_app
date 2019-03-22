from django.db import models
from django.urls import reverse


class Character(models.Model):
    """
    Character class.
    """
    character_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        """
        Return he character's name
        """
        return '{0}'.format(self.name)

    class Meta:
        db_table = 'character'
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('character-detail', args=[str(self.character_id)])
