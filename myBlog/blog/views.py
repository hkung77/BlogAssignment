from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import blogposts

# Create your views here.

def index(request):
    blog_list = blogposts.objects.order_by('-Pub_date')                 
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'blog_list' : blog_list 
    })
    return HttpResponse(template.render(context))
    
def detail(request, ID="0"):
    blog = blogposts.objects.get(id=ID)
    template = loader.get_template('blog/post.html')
    context = RequestContext(request, {
        'blog':blog,
    })
    return HttpResponse(template.render(context))
