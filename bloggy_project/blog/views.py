from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404
from blog.models import Post

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    popular_posts = Post.objects.all().order_by('-views')[:5]
    template = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts, 
        'popular_posts': popular_posts,
        }
    _remove_underscores_from_urls(latest_posts)
    _remove_underscores_from_urls(popular_posts)
    context = Context(context_dict)
    return HttpResponse(template.render(context))

def post(request, post_url):
    single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
    single_post.views += 1
    single_post.save()
    template = loader.get_template('blog/post.html')
    context = Context({'single_post': single_post, })
    return HttpResponse(template.render(context))

def _remove_underscores_from_urls(blog_posts):
    for blog_post in blog_posts:
        blog_post.url = _encode_url(blog_post.title)

def _encode_url(url):
    return url.replace(' ', '_')
