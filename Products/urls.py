from django.urls import path
from .views import *

urlpatterns=[
    path("",allProducts.as_view(),name="allproducts"),
    path("curd/<int:pk>",allView.as_view(),name="curd")
]