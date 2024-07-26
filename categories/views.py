from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


category_list = {
    "beauty": "Beauty Category",
    "food": "Food Category",
    "music": "Music Category",
    "science": "Science Category",
    "sports": "Sports Category",
    "technology": "Technology Category",
    "book": "Books Category"
}


def category_views(request, category):
    try:
        page_text = category_list[category]
        return HttpResponse(page_text)
    except:
        return HttpResponseNotFound("Invalid Category")


# Redirect Category by ID
def categories_id(request, category):
    category_id = list(category_list.keys())  # convert dictionary to list

    if category > len(category_id):
        return HttpResponseNotFound("Invalid Category")

    redirect_category = category_id[category - 1]
    redirect_path = reverse("category_name", args=[redirect_category])  # dynamic path using reverse
    return HttpResponseRedirect(redirect_path)
