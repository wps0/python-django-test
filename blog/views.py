from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


# Create your views here.
def post_list(req):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by("-publish_date")
    return render(req, "blog/post_list.html", {
        'posts': posts
    })


def post_view(req, post_id: int):
    post = get_object_or_404(klass=Post, id=post_id)
    if post.publish_date is None or post.publish_date > timezone.now():
        raise Http404("No Post matches the given query.")
    return render(req, "blog/post_view.html", {
        'post': post
    })
