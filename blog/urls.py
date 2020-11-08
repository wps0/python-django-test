from django.urls import path

# from blog import views
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_id>", views.post_view, name="post_view")
]
