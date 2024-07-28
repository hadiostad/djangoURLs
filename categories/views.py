from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

category_list = {
    "beauty": "Beauty Category",
    "food": "Food Category",
    "music": "Music Category",
    "science": "Science Category",
    "sports": "Sports Category",
    "technology": "Technology Category",
    "book": "Books Category"
}


def index(request):
    list_item = ""
    category_item = list(category_list.keys())  # convert dictionary to list

    for category in category_item:
        category_path = reverse("category_name", args=[category])
        list_item += f"<li><a href=\"{category_path}\">{category}</a></li>"

    response_data = f"<ol>{list_item}</ol>"
    return HttpResponse(response_data)


def category_views(request, category):
    try:
        category_description = category_list[category]
        return render(request, "categories/category.html", {
            "category_name": category.capitalize(),
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
