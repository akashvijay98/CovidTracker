from django.contrib import admin
from django.urls import include,path
from covidtracker import views

urlpatterns = [
    path('covidtracker/', include('covidtracker.urls')),
    path('admin/', admin.site.urls),
    path('export/', views.export),
    path('', views.simple_upload),
    path('index/',views.index),
    path('input/',views.input),
    path('update/',views.update),
    path('destroy/',view.destroy)
]
