from django.urls import path
from . import views

urlpatters = [
    path('', views.product_list),
]