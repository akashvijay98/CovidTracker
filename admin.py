from django.contrib import admin
from .models import covid_data
from import_export.admin import ImportExportModelAdmin

# Register your models here.


admin.site.register(covid_data)
class userdat(ImportExportModelAdmin):
    pass
