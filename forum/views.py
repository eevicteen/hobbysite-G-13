"""Receives web requests and returns the necessary web response."""
from django.shortcuts import render
from .models import Post, PostCategory


def forum_list(request):
    """Return forum_list html file with apt context."""
    categories = PostCategory.objects.all().order_by("name")
    posts = Post.objects.all().order_by("-creation_date")

    return render(request, "forum_list.html", {
        "postcategory": categories,
        "posts": posts
    })


def forum_details(request, id):
    """Return forum_details html file with apt context."""
    post = Post.objects.get(id=id)
    return render(request, "forum_details.html", {"post": post})