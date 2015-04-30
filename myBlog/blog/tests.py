from django.test import TestCase
from django.test import Client
from blog.models import blogposts
from django.utils import timezone
import unittest
# Create your tests here.

# Testing urls to make sure appropriate content is linked
class TestUrl(unittest.TestCase):
    def setUp(self):
        # Every test needs a client
        self.client = Client()
    def test_url(self):
        # Send blog url 
        response = self.client.get('/blog/')
        # Check if response is equal to 200
        self.assertEquals(response.status_code, 200)

# Testing if appropriate blog is returned to post.html
class TestDetails(unittest.TestCase):
    def setUp(self):
        # Every test needs a client
        self.client = Client()
        # Create fake data for database
        blogposts.objects.create(Title="test", Pub_date=timezone.now(), Description="Description Test", Text_link="LinkToText")
    def testPost(self):
        # Send request for post.html with id of fake data
        data =  blogposts.objects.get(Title="test")
        response = self.client.get('/blog/'+str(data.id)+'/')
        # Check if the returned blog post object has the name test
        self.assertEquals(response.context['blog'].Title, "test")
