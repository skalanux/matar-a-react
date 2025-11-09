from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("count/", views.count_sheep, name="count_sheep"),
]
