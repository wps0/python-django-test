from django.urls import path

# from blog import views
from . import views

urlpatterns = [
    path("", views.post_list, name="post_listing"),
    path("post/<int:post_id>", views.post_view, name="post_view"),
    path("post/new", views.post_new, name="post_new"),
    path("post/<int:post_id>/edit", views.post_edit, name="post_edit")
]
