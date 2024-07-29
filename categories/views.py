from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

category_list = {
    "beauty": "Beauty Category",
    "food": None,
    "music": "Music Category",
    "science": "Science Category",
    "sports": "Sports Category",
    "technology": "Technology Category",
    "book": "Books Category"
}


def index(request):
    category_item = list(category_list.keys())  # convert dictionary to list

    return render(request, "categories/index.html", {
        "category_item": category_item
    })


def category_views(request, category):
    try:
        category_description = category_list[category]
        return render(request, "categories/category.html", {
            "category_name": category,
            "category_description": category_description,

        })
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
