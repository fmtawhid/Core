from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def news(request):
    blog = postmodel.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'blog.html', context)



def singlenews(request, id):
    blogsingle = get_object_or_404(postmodel, pk = id)
    context = {
        'blogsingle':blogsingle
    }
    return render(request, 'blog-details.html', context)
