from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('detail/<int:pk>', Detail.as_view(), name="detail"),
    path('detail/<int:pk>/order/', FoodOrder.as_view(), name="order"),
    path('breakfast/', Breakfast.as_view(), name="breakfast"),
    path('lunch/', Lunch.as_view(), name="lunch"),
    path('dinner/', Dinner.as_view(), name="dinner"),
    path('fast-food/', FastFood.as_view(), name="fast_food"),
    path('persian/', Persian.as_view(), name="persian"),
    path('drinks/', Drinks.as_view(), name="drinks"),
    path('about-us/', AboutUs.as_view(), name="about_us"),
    path('contact-us/', contact_us, name="contact_us"),
]
