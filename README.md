# Init project 
package for rest api
```pip install djangorestframework```

register admin url
```py manage.py createsuperuser```



# Running services
py .\manage.py runserver

# (optional)
py .\manage.py makemigrations sr5_project_app 

py .\manage.py migrate

py .\manage.py sqlmigrate sr5_project_app 0001

<!-- Driver for mysql -->
pip install mysqlclient

<!-- Driver for pgsql -->
pip install psycopg2

<!-- Driver for oracle -->
pip install cx_Oracle

# Using Shell

py .\manage.py shell

from sr5_project_app.models import Article

# Pratices
Article.objects.all()
Article.objects.all().values()

x = Article()
x.title = 'Welcome to lulu'
x.content = 'Nice content'
x.save()
# Update the article
x = Article.objects.all()[0]
x.title = 'Love oun'
x.save()
x.delete()

y = Article(title='new title', content='Welcome to lulu')
y.save()

# quit shell
quit()

# Admin dashboard
=> should be migrate first
# Init for supper user
see documentation [How is python manage.py createsuperuser useful?](https://stackoverflow.com/questions/27472581/how-is-python-manage-py-createsuperuser-useful) 
py manage.py createsuperuser



# for imageFields
pip install Pillow
