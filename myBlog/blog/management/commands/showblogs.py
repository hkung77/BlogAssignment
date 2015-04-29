from django.core.management.base import BaseCommand, CommandError
from blog.models import blogposts

class Command(BaseCommand):
    # showall will display all the entries in the blog
    help = 'Displays all entries in the blog'

    def handle(self, *args, **options):
        try: 
            # Obtain all blog posts 
            blog_list = blogposts.objects.all()
        except blogposts.DoesNotExist:
            raise CommandError('blogposts does not exists') 

        # Set table template {column numer : width size}
        template = "{0:5} | {1:25} | {2:5} | {3:6} | {4:3} | {5:50}"
        print ""
        print template.format("ID", "Title", "Year", "Month", "Day", "Text Link")

        for blog in blog_list:
            print template.format(blog.id , blog.Title, blog.Pub_date.year,blog.Pub_date.month,blog.Pub_date.day, blog.Text_link)
        print"================================================================================="



