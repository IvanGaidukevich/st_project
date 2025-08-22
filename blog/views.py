from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment, PostStatus


def post_list(request):
    posts = Post.objects.all()
    return render(request,
                  template_name="list.html",
                  context={"posts": posts})


def post_detail(request, id, slug):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request,
                  template_name="detail.html",
                  context={"post": post})

