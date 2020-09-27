from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Nathaniel Vo', 
        'title': 'Blog Post',
        'content': 'first post', 
        'date_posted': '9/27/2020'
    },
    {
        'author': 'Nathaniel Vo\'s Twin', 
        'title': 'Blog Post 2',
        'content': 'second post', 
        'date_posted': '9/27/2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
