from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


categories = {
    "beauty": "Beauty Category",
    "food": "Food Category",
    "music": "Music Category",
    "science": "Science Category",
    "sports": "Sports Category",
    "technology": "Technology Category",
    "book": "Books Category"
}


def category_views(request, category):
    page_text = categories[category]
    return HttpResponse(page_text)


def categories_int(request, category):
    return HttpResponse(category)