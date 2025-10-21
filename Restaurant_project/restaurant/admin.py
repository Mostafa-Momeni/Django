from django.contrib import admin

from .models import *

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = list_display

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "old_price",
        "price",
    ]
    list_display_links = list_display
    filter_horizontal = ["food_type"]


@admin.register(SuggestionCritics)
class SuggestionCriticsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "text"
    ]
    list_display_links = list_display


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "food",
        "amount",
        "name",
        "phone_number",
        "email",
    ]
    list_display_links = list_display
    

