from django.urls import path
from . import views

# list of all urls
urlpatterns = [
    # Url Config
    # dynamic path segments
    path("<category>", views.categories),

]