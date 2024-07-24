# Django CRUD Tutorial 🚀

Welcome to the Django CRUD tutorial! This guide will walk you through creating a simple CRUD (Create, Read, Update, Delete) application using Django, from setting up your environment to deploying a functional web application.

## Table of Contents 📚

1. [Setup and Installation](#setup-and-installation-)
2. [Project and App Structure](#project-and-app-structure-)
3. [Creating Views](#creating-views-)
4. [Setting Up URLs](#setting-up-urls-)
5. [Templates and Static Files](#templates-and-static-files-)
6. [Creating Models](#creating-models-)
7. [Admin Interface](#admin-interface-)
8. [Displaying Data on the Frontend](#displaying-data-on-the-frontend-)
9. [Implementing Relationships](#implementing-relationships-)
10. [Django Forms](#django-forms-)
11. [Working with URL Parameters](#working-with-url-parameters-)
12. [Customizing the User Model](#customizing-the-user-model-)
13. [Adding Update and Delete Functionality](#adding-update-and-delete-functionality-)
14. [Conclusion](#conclusion-)

## Setup and Installation 🔧

Let's kick off by setting up our development environment and installing the necessary packages.

### Using UV for Package Installation ⚡

UV is a faster alternative to pip, built with Rust for efficiency.

1. **Install UV:**
   ```sh
   pip install uv
   ```
2. **Create a Virtual Environment:**
   ```sh
   uv venv
   ```
3. **Activate the Virtual Environment:**
   ```sh
   .venv/Scripts/Activate
   ```
4. **Deactivate the Virtual Environment:**
   ```sh
   deactivate
   ```
5. **Install Django:**
   ```sh
   uv pip install Django
   ```

### Setting Up the Django Project 🌟

1. **Start a New Project:**
   ```sh
   django-admin startproject crud
   ```
2. **Navigate to the Project Directory:**
   ```sh
   cd crud
   ```
3. **Run the Server:**
   ```sh
   python manage.py runserver
   ```
   Optionally, run the server on a specific port:
   ```sh
   python manage.py runserver [Port Number]
   ```

## Project and App Structure 🏗️

Understanding the structure of a Django project is crucial for efficient development.

### Project Structure Overview 🗂️

- **`manage.py`**: The entry point for the project, containing environment variables and settings.
- **Root Level**: Contains the project folder (`crud`), which houses settings, URLs, and WSGI files.
- **Application Level**: Contains individual apps that handle different aspects of the project.

### Creating a Django App 🛠️

1. **Create an App:**
   ```sh
   python manage.py startapp appname
   ```
2. **Configure the App in `settings.py`:**
   ```python
   INSTALLED_APPS = [
       ...
       'appname',
   ]
   ```

### Changing the Database 🔄

Django supports multiple databases like PostgreSQL, MySQL, and SQLite. Modify the database settings in `settings.py` to switch databases.

## Creating Views 👁️

Views are essential for handling requests and returning responses.

### Creating the `views.py` File 📄

Define views in `views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
```

### Adding More Functions ➕

Create additional functions in `views.py` as needed.

## Setting Up URLs 🔗

URLs are the entry points to your views.

### Configuring URL Patterns 🔍

1. **Import Views:**
   ```python
   from . import views
   ```
2. **Add URL Paths in `urls.py`:**

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
   ]
   ```

### Using Namespaces 🌐

Use the `name` parameter for URL patterns to refer to them in templates and views.

## Templates and Static Files 🎨

Templates and static files are crucial for rendering HTML and serving CSS, JavaScript, and images.

### Creating Templates 🖌️

1. **Create a `templates` Folder:**

   - Create a folder named `templates` in the root directory.
   - Add HTML files in the `templates` folder.

2. **Render Templates in Views:**

   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'index.html')
   ```

### Managing Static Files 📁

1. **Create a `static` Folder:**

   - Create a folder named `static` in the root directory.
   - Add subfolders for CSS, JS, and other static files.

2. **Link Static Files in Templates:**

   ```html
   {% load static %}
   <link rel="stylesheet" href="{% static 'css/style.css' %}" />
   ```

3. **Configure Static and Media Files in `settings.py`:**

   ```python
   STATIC_URL = 'static/'
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

   MEDIA_URL = 'media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

### Example: Adding a CSS File 💅

Create a file named `style.css` under the `static/css` directory:

```css
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
}
```

Link the CSS file in your template:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
  </head>
  <body>
    <h1>Welcome to Django CRUD Tutorial</h1>
  </body>
</html>
```

## Creating Models 🗂️

Models represent the database structure.

### Defining Models 📝

Create models in `models.py`:

```python
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
```

### Installing Pillow for Image Fields 🖼️

Install Pillow for handling image fields:

```sh
pip install Pillow
```

### Running Migrations ⚙️

1. **Create Migrations:**
   ```sh
   python manage.py makemigrations
   ```
2. **Apply Migrations:**
   ```sh
   python manage.py migrate
   ```

### Example: Adding a Blog Model 📝

```python
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

Register the model in `admin.py`:

```python
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)
```

## Admin Interface 🛠️

Django's admin interface is a powerful tool for managing your application's data.

### Creating a Superuser 🧑‍💻

Create a superuser to access the admin panel:

```sh
python manage.py createsuperuser
```

### Registering Models in Admin 📋

Register models in `admin.py`:

```python
from django.contrib import admin
from .models import UserDetails

admin.site.register(UserDetails)
```

### Customizing the Admin Interface 🎨

Customize the admin display:

```python
class AdminPaneDisplayUserDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'image')
    search_fields = ('name', 'email', 'password', 'image')

admin.site.register(UserDetails, AdminPaneDisplayUserDetails)
```

### Example: Adding Custom Actions 🚀

```python
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    actions = ['publish']

    def publish(self, request, queryset):
        queryset.update(published_date=timezone.now())
    publish.short_description = "Mark selected blogs as published"

admin.site.register(Blog, BlogAdmin)
```

## Displaying Data on the Frontend 📄

Learn how to query and display data on the frontend.

### Querying Data in Views 🕵️‍♂️

Query data and pass it to templates:

```python
def user_list(request):
    users = UserDetails.objects.all()
    return render(request, 'user_list.html', {'users': users})
```

### Displaying Data in Templates 🌐

Use Jinja for loops to display data:

```html
{% for user in users %}
<p>{{ user.name }}</p>
{% endfor %}
```

### Example: Displaying Blog Posts 📄

```python
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})
```

```html
{% for blog in blogs %}
<h2>{{ blog.title }}</h2>
<p>{{ blog.content }}</p>
<small>Published on: {{ blog.published_date }}</small>
{% endfor %}
```

## Implementing Relationships 🤝

Django supports various types of relationships.

### Defining Relationships in Models 💑

Define One-to-One, One-to

-Many, and Many-to-Many relationships:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### Example: Adding Comments to Blog Posts 📝

```python
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

## Django Forms 📝

Forms are essential for handling user input.

### Creating Forms 🖊️

Create a form in `forms.py`:

```python
from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'email', 'password', 'image']
```

### Rendering Forms in Templates 📄

Render forms in templates:

```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Submit</button>
</form>
```

### Handling Form Submissions 🚀

Handle form submissions in views:

```python
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})
```

### Example: Creating a Blog Post Form 📝

```python
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
```

```python
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})
```

## Working with URL Parameters 🔗

URL parameters are useful for passing data to views.

### Using URL Parameters 🔄

Define URL parameters in `urls.py`:

```python
urlpatterns = [
    path('user/<int:id>/', views.user_detail, name='user_detail'),
]
```

### Handling URL Parameters in Views 🌐

Retrieve URL parameters in views:

```python
def user_detail(request, id):
    user = get_object_or_404(UserDetails, id=id)
    return render(request, 'user_detail.html', {'user': user})
```

### Example: Displaying a Single Blog Post 📄

```python
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})
```

## Customizing the User Model 👥

Customize the default user model to fit your needs.

### Extending the User Model 🛠️

Create a custom user model:

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
```

### Updating `settings.py` 🔄

Update the `AUTH_USER_MODEL` setting:

```python
AUTH_USER_MODEL = 'appname.CustomUser'
```

### Creating User Forms 📝

Create forms for user registration and authentication.

### Example: Custom User Registration Form 📝

```python
from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone']
```

## Adding Update and Delete Functionality 🔄

Enhance your CRUD application by adding update and delete features.

### Update Functionality 🛠️

1. **Update View:**

   - Add a view function in `views.py` for updating user details.

   ```python
   from django.shortcuts import render, get_object_or_404, redirect
   from .models import UserDetails
   from .forms import UserForm

   def update_user(request, id):
       user = get_object_or_404(UserDetails, id=id)
       if request.method == "POST":
           form = UserForm(request.POST, request.FILES, instance=user)
           if form.is_valid():
               form.save()
               return redirect('user_list')
       else:
           form = UserForm(instance=user)
       return render(request, 'update_user.html', {'form': form})
   ```

2. **Update Template:**

   - Create an `update_user.html` template.

   ```html
   <h2>Update User</h2>
   <form method="post" enctype="multipart/form-data">
     {% csrf_token %} {{ form.as_p }}
     <button type="submit">Update</button>
   </form>
   ```

3. **Update URL:**

   - Add the URL pattern for the update view in `urls.py`.

   ```python
   urlpatterns = [
       ...
       path('user/update/<int:id>/', views.update_user, name='update_user'),
   ]
   ```

### Delete Functionality 🗑️

1. **Delete View:**

   - Add a view function in `views.py` for deleting user details.

   ```python
   from django.shortcuts import render, get_object_or_404, redirect
   from .models import UserDetails

   def delete_user(request, id):
       user = get_object_or_404(UserDetails, id=id)
       if request.method == "POST":
           user.delete()
           return redirect('user_list')
       return render(request, 'delete_user.html', {'user': user})
   ```

2. **Delete Template:**

   - Create a `delete_user.html` template.

   ```html
   <h2>Are you sure you want to delete this user?</h2>
   <form method="post">
     {% csrf_token %}
     <button type="submit">Delete</button>
   </form>
   ```

3. **Delete URL:**

   - Add the URL pattern for the delete view in `urls.py`.

   ```python
   urlpatterns = [
       ...
       path('user/delete/<int:id>/', views.delete_user, name='delete_user'),
   ]
   ```

### Example: Update and Delete Blog Posts 📝

```python
# views.py
from .models import Blog
from .forms import BlogForm

def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'update_blog.html', {'form': form})

def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')
    return render(request, 'delete_blog.html', {'blog': blog})
```

```python
# urls.py
urlpatterns = [
    ...
    path('blog/update/<int:id>/', views.update_blog, name='update_blog'),
    path('blog/delete/<int:id>/', views.delete_blog, name='delete_blog'),
]
```

```html
<!-- update_blog.html -->
<h2>Update Blog</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Update</button>
</form>
```

```html
<!-- delete_blog.html -->
<h2>Are you sure you want to delete this blog post?</h2>
<form method="post">
  {% csrf_token %}
  <button type="submit">Delete</button>
</form>
```

## Conclusion 🎉

Congratulations! You've successfully built a Django CRUD application with create, read, update, and delete functionality. This tutorial covered the basics, and now you can expand on it to build more complex applications. Keep exploring Django's documentation and features to enhance your skills further. Happy coding!
