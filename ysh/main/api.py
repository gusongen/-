from django.urls import path, include
from . import views

urlpatterns = [

    # API
    path("item/", views.item),
    path("pic/", views.image_requester),
    path("likeitem/", views.like_item),
]
