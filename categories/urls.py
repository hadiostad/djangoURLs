from django.urls import path
from . import views

# list of all urls
urlpatterns = [
    path('beauty', views.index), # Url Config
]