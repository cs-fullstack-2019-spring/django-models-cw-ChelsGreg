from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# FUNCTION FOR ROUTE
def index(request):
    return HttpResponse("WHAT'S UP!")