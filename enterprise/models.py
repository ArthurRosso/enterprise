from django.db import models
import datetime

class Poster(models.Model):
    
    # Language of the starwheel
    lang = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    # Text above the starwheel
    text = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    # Reason that makes the day special
    reason = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    # City
    city = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    # Date 
    date = models.DateField(
        default=datetime.date.today,
        null=False,
        blank=False
    )
    
    # Starwheel
    st = models.BinaryField(
        blank=True
    )

    objetos = models.Manager()