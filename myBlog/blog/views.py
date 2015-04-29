from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import logging

from .models import blogposts

# Create your views here.

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
# This function returns index.html ( the home page )
    try:
        # Obtain all objects in the blog database
        blog_list = blogposts.objects.order_by('-Pub_date')     
    except blogposts.DoesNotExists: 
        raise CommandError('blogposts does not exists')
        logger.error('Attempting to access blogposts. Error: blogposts database does not exists')

    # Set index.html as the template
    template = loader.get_template('blog/index.html')       

    # Set the appropriate keyword for index.html
    context = RequestContext(request, {
        'blog_list' : blog_list                             
    })
    return HttpResponse(template.render(context))
    
def detail(request, ID="0"):
# This function is used for viewing individual blog posts
    try:
        # Obtain individual blog post via primary key
        blog = blogposts.objects.get(id=ID)                     
    except blogposts.id.DoesNotExists:
        # If primary key does not exists, blog is not in the database
        raise CommandError('blog post with '+ID+' does not exists in database')
        logger.error('Attempting to access blog post with '+ID+'. Error: ' +ID+' does not exists')
    # Set post.html as the template
    template = loader.get_template('blog/post.html')        

    # Set the appropriate keyword for post.html
    context = RequestContext(request, {
        'blog':blog,                                        
    })
    return HttpResponse(template.render(context))
