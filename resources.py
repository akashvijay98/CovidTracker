from import_export import resources
from .models import covid_data

class dataResource(resources.ModelResource):
    class Meta:
        model = covid_data