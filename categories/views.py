from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def categories(request, category):
    page_text = None
    if category == "beauty":
        page_text = "Beauty category"
    elif category == "book":
        page_text = "Book category"
    elif category == "electronics":
        page_text = "Electronics category"
    else:
        return HttpResponseNotFound("This Category Invalid")
    return HttpResponse(page_text)