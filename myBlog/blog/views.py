from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import blogposts

# Create your views here.

def index(request):
# This function returns index.html ( the home page )
    blog_list = blogposts.objects.order_by('-Pub_date')     # Obtain all objects in the blog database
    template = loader.get_template('blog/index.html')       # Set index.html as the template
    context = RequestContext(request, {
        'blog_list' : blog_list                             # Set the appropriate keyword for index.html
    })
    return HttpResponse(template.render(context))
    
def detail(request, ID="0"):
# This function is used for viewing individual blog posts
    blog = blogposts.objects.get(id=ID)                     # Obtain individual blog post via primary key
    template = loader.get_template('blog/post.html')        # Set post.html as the template
    context = RequestContext(request, {
        'blog':blog,                                        # Set the appropriate keyword for post.html
    })
    return HttpResponse(template.render(context))
