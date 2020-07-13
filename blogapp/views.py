from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog_Article
# Create your views here.
def index(request):
    blogs = Blog_Article.objects.all()
    return render(request,'index.html',{'blogs': blogs})


def post(request):
    if request.method == 'POST':

        blogs = Blog_Article()
        blogs.title = request.POST['title']
        blogs.content = request.POST['content']
        blogs.author = request.user
        blogs.save()
                
        return redirect('/',{'blogs':blogs })  

    else:
        return render(request,'post.html')