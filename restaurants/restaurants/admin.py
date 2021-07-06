from django.contrib import admin
from .models import Restaurant, Pizza


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant

class PizzaAdmin(admin.ModelAdmin):
    model = Pizza

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Pizza, PizzaAdmin)