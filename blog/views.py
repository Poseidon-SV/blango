import logging

from django.shortcuts import render

from django.utils import timezone
from blog.models import Post

from django.shortcuts import render, get_object_or_404

from django.views.decorators.cache import cache_page  
from django.views.decorators.vary import vary_on_cookie
# Create your views here.

def index(request):
    # posts = Post.objects.filter(published_at__lte=timezone.now())
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    
    logger.debug("Got %d posts", len(posts))

    return render(request, "blog/index.html", {"posts": posts})

# def index(request):
#     from django.http import HttpResponse
#     return HttpResponse(str(request.user).encode("ascii"))
#     posts = Post.objects.filter(published_at__lte=timezone.now())
#     logger.debug("Got %d posts", len(posts))
#     return render(request, "blog/index.html", {"posts": posts})

# @cache_page(300)

# # @vary_on_headers("Cookie")
# @vary_on_cookie
# def index(request):
#     from django.http import HttpResponse
#     return HttpResponse(str(request.user).encode("ascii"))
#     posts = Post.objects.filter(published_at__lte=timezone.now())
#     logger.debug("Got %d posts", len(posts))
#     return render(request, "blog/index.html", {"posts": posts})


    

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
)

    return render(request, "blog/post-detail.html", {"post": post})

logger = logging.getLogger(__name__)

# logger.debug("Got %d posts", len(posts))
# logger.info(
#     "Created comment on Post %d for user %s", post.pk, request.user
# )

# @cache_page(300)
# def index(request):
#     # existing view code

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])