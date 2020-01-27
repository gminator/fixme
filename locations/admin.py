from django.contrib import admin
from .models import *

from mapwidgets.widgets import GooglePointFieldInlineWidget
from mapwidgets.widgets import GooglePointFieldWidget
import floppyforms as forms



class MultiPolygonWidget(forms.gis.MultiPolygonWidget, forms.gis.BaseGMapWidget):
    google_maps_api_key = 'AIzaSyBgl8yQm01JHngHx4zVb1ylrpgtcVSOtt0'
    default_zoom = False
    

CUSTOM_MAP_SETTINGS = { 
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocation", [-33.9248685, 18.424055299999964]),
    ),
    "GOOGLE_MAP_API_KEY" : "AIzaSyBgl8yQm01JHngHx4zVb1ylrpgtcVSOtt0"
}

# Register your models here.
class LocationAdmin(admin.ModelAdmin): 
    list_display= ('name',) 
    #MultiDwellingUnit.import_all()

    #def package(self, obj):
    #    return obj.service_profile_name

    #Order.import_all_orders()
    formfield_overrides = {
         models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)},
         models.MultiPolygonField: {"widget": MultiPolygonWidget(attrs={"default_zoom" : 19, "default_lon" : 20, "default_lat" : 20})}
    }

admin.site.register(Location,LocationAdmin)
