from django.shortcuts import render, get_object_or_404

from contents.models import PostContent, Post


def home(request):
    return render(request, 'home.html')

def about(request):
    a = 'This is an about page'

    return render(request, 'about.html' , context={'a':a})

def posts(request):
    posts = Post.objects.all()  # barcha postlarni oladi
    if posts.exists():
        return render(request, 'posts.html', context={'posts': posts})
    else:
        return render(request, 'home.html', context={'posts': posts})
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', context={'post': post})