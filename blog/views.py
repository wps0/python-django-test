from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.forms import PostForm
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


def post_new(req):
    if req.user is None or req.user.is_authenticated:
        raise PermissionDenied

    if req.method == "POST":
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_view', pk=post.pk)
    else:
        form = PostForm()
    return render(req, 'blog/post_edit.html', {
        'form': form
    })


def post_edit(req, post_id: int):
    if req.user is None or req.user.is_authenticated:
        raise PermissionDenied

    post = get_object_or_404(klass=Post, id=post_id)
    if req.method == "POST":
        form = PostForm(req.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_view', post_id=post.id)
        else:
            form = PostForm(instance=post)
    else:
        form = PostForm(instance=post)
    return render(req, 'blog/post_edit.html', {
        'form': form
    })
