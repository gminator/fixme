from django.db import models
from django.contrib.gis.geos import Polygon, MultiPolygon, LinearRing
from django.contrib.gis.db import models

# Create your models here.

class Location(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    location = models.PointField(default='POINT(0.0 0.0)') 
    mpoly = models.MultiPolygonField()
