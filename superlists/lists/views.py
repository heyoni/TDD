from django.http import HttpResponse
from django.shortcuts import render


# home_page=None


def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title>')