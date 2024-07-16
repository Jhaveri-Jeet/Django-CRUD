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
11. [Conclusion](#conclusion-)

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

Define One-to-One, One-to-Many, and Many-to-Many relationships:

```python
class UserMoreDetails(models.Model):
    user = models.OneToOne

Field(UserDetails, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
```

### Example: Many-to-Many Relationship with Tags 🏷️

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
```

## Django Forms 📝

Forms are essential for handling user input.

### Creating Forms 📑

Django provides two types of forms: `forms.Form` and `forms.ModelForm`. Here, we'll explore both.

### `forms.Form` Example

Use `forms.Form` when you need full control over form fields and processing, especially when the form is not directly tied to a model.

1. **Define the Form:**

   ```python
   from django import forms

   class NameForm(forms.Form):
       your_name = forms.CharField(label="Your name", max_length=100)
   ```

2. **Handling Form Submissions in Views:**

   ```python
   def name_form_view(request):
       if request.method == 'POST':
           form = NameForm(request.POST)
           if form.is_valid():
               # Process the data
               name = form.cleaned_data['your_name']
               # Do something with the name
               return HttpResponse(f"Hello, {name}")
       else:
           form = NameForm()
       return render(request, 'name_form.html', {'form': form})
   ```

3. **Rendering Forms in Templates:**

   ```html
   <form method="post">
     {% csrf_token %} {{ form.as_p }}
     <button type="submit">Submit</button>
   </form>
   ```

### `forms.ModelForm` Example

Use `forms.ModelForm` when the form is directly tied to a model and you want to save or update model instances.

1. **Define the Form:**

   ```python
   from django import forms
   from .models import UserDetails

   class UserForm(forms.ModelForm):
       class Meta:
           model = UserDetails
           fields = ['name', 'image']
           widgets = {
               'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
               'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
           }
           labels = {
               'name': 'Full Name',
               'image': 'Profile Picture',
           }
           help_texts = {
               'name': 'Please enter your full name.',
               'image': 'Upload a profile picture.',
           }
           error_messages = {
               'name': {
                   'max_length': 'Name is too long.',
                   'required': 'Name is required.',
               },
               'image': {
                   'invalid': 'Invalid image format.',
               },
           }
   ```

2. **Handling Form Submissions in Views:**

   ```python
   def user_create(request):
       if request.method == 'POST':
           form = UserForm(request.POST, request.FILES)
           if form.is_valid():
               form.save()
               return redirect('user_list')
       else:
           form = UserForm()
       return render(request, 'user_form.html', {'form': form})
   ```

3. **Rendering Forms in Templates:**

   ```html
   <form method="post" enctype="multipart/form-data">
     {% csrf_token %} {{ form.as_p }}
     <button type="submit">Save</button>
   </form>
   ```

### Differences Between `forms.Form` and `forms.ModelForm`

- **Use Case:**

  - **`forms.Form`**: Use when you need full control over form fields and processing, and the form is not directly tied to a model.
  - **`forms.ModelForm`**: Use when the form is directly tied to a model and you want to create or update model instances.

- **Field Definition:**

  - **`forms.Form`**: Manually define each field in the form.
  - **`forms.ModelForm`**: Automatically generates form fields based on the model fields.

- **Validation:**

  - **`forms.Form`**: Manually handle validation logic.
  - **`forms.ModelForm`**: Leverages model validation logic, reducing boilerplate code.

- **Saving Data:**

  - **`forms.Form`**: Manually handle the saving of data.
  - **`forms.ModelForm`**: Automatically handles saving of model instances.

- **Boilerplate Code:**
  - **`forms.Form`**: Requires more boilerplate code to handle fields, validation, and saving data.
  - **`forms.ModelForm`**: Reduces boilerplate code by leveraging model fields and validation.

### Example: Blog Post Form 📝

Using `forms.ModelForm` to create a blog post form:

1. **Define the Form:**

   ```python
   from django import forms
   from .models import Blog

   class BlogForm(forms.ModelForm):
       class Meta:
           model = Blog
           fields = ['title', 'content', 'tags']
   ```

2. **Handling Form Submissions in Views:**

   ```python
   def blog_create(request):
       if request.method == 'POST':
           form = BlogForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('blog_list')
       else:
           form = BlogForm()
       return render(request, 'blog_form.html', {'form': form})
   ```

3. **Rendering Forms in Templates:**

   ```html
   <form method="post">
     {% csrf_token %} {{ form.as_p }}
     <button type="submit">Save</button>
   </form>
   ```

## Conclusion 🏁

Congratulations! You have successfully created a CRUD application using Django. This tutorial covered the basics of setting up a Django project, creating models, views, and templates, handling form submissions, and customizing the admin interface. With these skills, you can build more complex applications and continue exploring Django's powerful features.

Feel free to contribute to this repository, report issues, or ask questions. Happy coding! 🎉
