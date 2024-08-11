from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from Blog.models import Post

# Create your views here.
def index(request):
    # posts = Post.objects.filter(published_at__lte=timezone.now())
    posts = Post.objects.all()
    return render(request, "Blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "Blog/post-detail.html", {"post":post})
