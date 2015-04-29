from django.contrib import admin

# Register your models here.

from .models import blogposts

admin.site.register(blogposts)
