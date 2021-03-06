from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class ComicStrip(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1} {2}'.format(self.title, self.author.first_name, self.author.last_name)

class ComicStripFrame(models.Model):
    comic_strip = models.ForeignKey(ComicStrip, on_delete=models.CASCADE)
    narrative = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images')
    sequence = models.IntegerField(null=False, blank=False)
    move = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{0}-{1}: {2}'.format(self.comic_strip.title,
                                     'Frame',
                                     self.sequence)
