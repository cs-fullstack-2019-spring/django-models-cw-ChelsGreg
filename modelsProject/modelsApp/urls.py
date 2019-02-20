from django.urls import path
from . import views

# DIRECTING ROUTE
urlpatterns= [
    path("", views.index, name="index"),
]