from django.shortcuts import render

posts = [
    {
        'author': 'Zhoosh',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 6, 2016'
    },
    {
        'author': 'Melonman',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 7, 2016'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
