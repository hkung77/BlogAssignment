# BlogAssignment

This blog is used to show blog posts in a list view as well as a detail view.
Created using Django, and Bootstrap.

----------
HTML Files
----------
index.html  : - shows the title and a short description of each blog post in a list view
              - blogs are sorted by date published
              
post.html   : shows individual blog posts including the title, date of publication, and the content

--------------------------------
Customized django-admin commands
--------------------------------
showblogs.py : 
  HOW TO RUN : python manage.py showblogs
    - This function displays all blog posts stored in the database in a well formated table. 
    - The table is formatted in this order:   ID | Title | Year | Month | Date | Text Link

---------    
models.py 
---------
This blog has a single model called blogposts.
Here are the data fields for the model :
    Title         : CharField with max size of 200
    Pub_date      : DateTimeField
    Description   : CharField with max size of 200
    Text_link     : CharField with max size of 200
    
--------
views.py
--------
This view contains 2 functions :
  - index
       Used for the index.html 
       Returns a list of all blogs in the database
  
  - detail
     Used for post.html
     Takes 1 parameter ID ( corresponds to the primary key of the blog )
     Returns a single blog that matches the corresponding ID 

