Sure! Let's enhance your Django CRUD tutorial by including details on sending data through the GET method (via URL parameters) and changing the user model in Django.

---

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
13. [Conclusion](#conclusion-)

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

### Def

ining Relationships 💍

Define relationships in models:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### Querying Relationships 🔍

Query related objects:

```python
def author_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = author.book_set.all()
    return render(request, 'author_books.html', {'author': author, 'books': books})
```

### Displaying Related Data in Templates 🌐

Display related data:

```html
<h2>{{ author.name }}</h2>
<ul>
  {% for book in books %}
  <li>{{ book.title }}</li>
  {% endfor %}
</ul>
```

### Example: Many-to-Many Relationship 👫

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student)
```

## Django Forms 📝

Forms are crucial for user input.

### Creating Forms 📝

Create forms in `forms.py`:

```python
from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'email', 'password', 'image']
```

### Handling Form Submissions 📨

Handle form submissions in views:

```python
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})
```

### Displaying Forms in Templates 🌐

Display forms in templates:

```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Create User</button>
</form>
```

### Example: Contact Form 📨

```python
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

```python
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

## Working with URL Parameters 🔗

URL parameters are useful for dynamic views and passing data through URLs.

### Using Path Parameters 🌐

Capture parameters in URLs:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:id>/', views.user_detail, name='user_detail'),
]
```

Handle the parameters in views:

```python
def user_detail(request, id):
    user = UserDetails.objects.get(id=id)
    return render(request, 'user_detail.html', {'user': user})
```

### Example: Search Functionality 🔍

Capture search parameters:

```python
def search(request):
    query = request.GET.get('q')
    results = UserDetails.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results})
```

### Displaying Search Results 🌐

```html
<form method="get" action="{% url 'search' %}">
  <input type="text" name="q" placeholder="Search users..." />
  <button type="submit">Search</button>
</form>

{% for user in results %}
<p>{{ user.name }}</p>
{% endfor %}
```

## Customizing the User Model 🧑‍💻

Django allows you to customize the user model to suit your needs.

### Creating a Custom User Model 📝

Create a custom user model in `models.py`:

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
```

### Updating Settings ⚙️

Update settings to use the custom user model:

```python
AUTH_USER_MODEL = 'appname.CustomUser'
```

### Creating Custom User Forms 📝

Create forms for the custom user model:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name')
```

### Updating Admin Interface 🛠️

Update the admin interface to use the custom user model:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
```

## Conclusion 🎉

Congratulations! You have successfully created a Django CRUD application. This tutorial covered setting up a Django project, creating models, views, and templates, and working with URL parameters and custom user models. Keep exploring Django to build more advanced features and applications.

Happy Coding! 🎉
