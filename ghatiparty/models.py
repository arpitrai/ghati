from django.db import models

class Songs(models.Model):
    GHATI_CHOICES = (
            (u'G1', u'I\'m too Cool for This'),
            (u'G2', u'Ghatipan in Control'),
            (u'G3', u'Ghatipan Heaven'),
            )
    artist = models.CharField(blank=True, max_length=100)
    title = models.CharField(max_length=200)
    url = models.URLField(verify_exists=False)
    duration = models.DecimalField(max_digits=7, decimal_places=2)
    mood = models.CharField(max_length=2, choices=GHATI_CHOICES)
    created_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title + ' by ' + self.artist
