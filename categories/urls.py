from django.urls import path
from . import views

# list of all urls
urlpatterns = [
    # Url Config
    # dynamic path segments
    path("<int:category>", views.categories_int),
    path("<str:category>", views.category_views)


]