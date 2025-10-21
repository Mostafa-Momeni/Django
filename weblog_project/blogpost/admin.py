from django.contrib import admin
from .models import BlogPost,Comments



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "titel",
        "datetime_created",
        "datetime_modified",
        # "likes",
        "author",
    ]

    list_display_links = [
        "titel",
        "datetime_created",
        "datetime_modified",
        # "likes",
        "author",
    ]
    
    filter_horizontal = ["likes"]

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display= [
        "name",
        "hide_name",
        "post",
        "comment",
        "state",
        "datetime_created",
        "datetime_modified",
    ]
    
    list_display_links= [
        "name",
        "hide_name",
        "post",
        "datetime_created",
        "datetime_modified",
    ]
    list_editable = ["state"]