from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import logging

from .models import blogposts

# Create your views here.

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
# This function corresponds to index.html ( the home page )
# It returns a list of all blogs in the database to index.html in a list view
    try:
        # Obtain all objects in the blog database
        blog_list = blogposts.objects.order_by('-Pub_date')     
    except blogposts.DoesNotExists: 
        # Raise and error and log 
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
# It takes 1 parameter ID (defaulted to 0) which corresponds to the primary key of each blog post in the database
# Returns a single blog post with the corresponding ID with the detailed view of the blog
    try:
        # Obtain individual blog post via primary key
        blog = blogposts.objects.get(id=ID)                     
    except blogposts.id.DoesNotExists:
        # If primary key does not exists, blog is not in the database
        # Raise and error and log 
        raise CommandError('blog post with '+ID+' does not exists in database')
        logger.error('Attempting to access blog post with '+ID+'. Error: ' +ID+' does not exists')
    # Set post.html as the template
    template = loader.get_template('blog/post.html')        

    # Set the appropriate keyword for post.html
    context = RequestContext(request, {
        'blog':blog,                                        
    })
    return HttpResponse(template.render(context))
