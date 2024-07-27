from django.urls import path
from . import views

# list of all urls
urlpatterns = [
    # Url Config
    path("", views.index),  # categories page
    # dynamic path segments
    path("<int:category>", views.categories_id),
    path("<str:category>", views.category_views, name="category_name")
]