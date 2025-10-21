from django.urls import path
from .views import *

# Functional based
# urlpatterns = [
    # path('', home, name="home"),
    # path('add/', add, name="add"),
    # path('detail/<int:pk>', detail, name="detail"),
    # path('delete/<int:pk>', delete, name="delete"),
    # path('update/<int:pk>', update, name="update"),
    # path('recent_posts/', recent_posts, name="recent_posts"),
    # path('favorites/', favorites, name="favorites"),
    # path('myposts/', my_posts, name="my_posts"),
# ] 

# Class based
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('add/', Add.as_view(), name="add"),
    path('detail/<int:pk>', Detail.as_view(), name="detail"),
    path('delete/<int:pk>', Delete.as_view(), name="delete"),
    path('update/<int:pk>', Update.as_view(), name="update"),
    path('recent_posts/', RecentPosts.as_view(), name="recent_posts"),
    path('favorites/', Favorites.as_view(), name="favorites"),
    path('myposts/', MyPosts.as_view(), name="my_posts"),
] 

