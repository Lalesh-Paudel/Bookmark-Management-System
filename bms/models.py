from django.db import models
from django.db.models.base import Model

# Create your models here.

class bookmarkList(models.Model):
    site_name = models.CharField(max_length=200)
    url       = models.URLField(max_length=500)
    category  = models.CharField(max_length=200)

    def __str__(self):
        return self.site_name

