from django.urls import path, include
from . import views

urlpatterns = [

    #API
    path("item/",views.item),
]
