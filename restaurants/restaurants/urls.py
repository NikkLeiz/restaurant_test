from django.contrib import admin
from django.urls import path, include
from .views import listRestaurants, restaurantDetail, listPizzas, pizzaDetail

urlpatterns = [
    path('restaurants/', listRestaurants.as_view()),
    path('restaurants/<int:id>/', restaurantDetail.as_view()),
    path('pizzas/', listPizzas.as_view()),
    path('pizzas/<int:id>/', pizzaDetail.as_view()),
]
