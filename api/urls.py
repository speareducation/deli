# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from api import views

urlpatterns = [
    path('api/v1/sandwiches/', views.SandwichList.as_view()),
    path('api/v1/sandwiches/<int:pk>/', views.SandwichDetail.as_view()),
    path('api/v1/toppings/', views.ToppingList.as_view()),
    path('api/v1/toppings/<int:pk>/', views.ToppingDetail.as_view()),
    path('api/v1/sandwiches/<int:pk>/toppings', views.SandwichToppingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)