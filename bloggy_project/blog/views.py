from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect

from blog.models import Post
from blog.forms import PostForm

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    popular_posts = Post.objects.all().order_by('-views')[:5]
    template = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
        }
    context = Context(context_dict)
    return HttpResponse(template.render(context))

def post(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1
    single_post.save()
    template = loader.get_template('blog/post.html')
    context = Context({'single_post': single_post, })
    return HttpResponse(template.render(context))

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(index)
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})
