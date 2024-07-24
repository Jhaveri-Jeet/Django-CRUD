# Django CRUD Tutorial 🚀

Welcome to the Django CRUD tutorial! This guide will take you through creating a simple CRUD (Create, Read, Update, Delete) application using Django. We'll cover everything from setting up your environment to deploying a fully functional web application.

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
14. [Adding Pagination](#adding-pagination-)
15. [Adding Search Functionality](#adding-search-functionality-)
16. [Conclusion](#conclusion-)

## Setup and Installation 🔧

### Using UV for Package Installation ⚡

UV is a modern, faster alternative to pip, built with Rust for efficiency.

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

Understanding the structure of a Django project is essential for effective development.

### Project Structure Overview 🗂️

- **`manage.py`**: The entry point for the project, containing environment variables and settings.
- **Root Level**: Contains the project folder (`crud`), which includes settings, URLs, and WSGI files.
- **Application Level**: Houses individual apps that handle different aspects of the project.

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

Django supports various databases like PostgreSQL, MySQL, and SQLite. Modify the database settings in `settings.py` to switch databases.

## Creating Views 👁️

Views handle requests and return responses.

### Creating the `views.py` File 📄

Define views in `views.py`:

```python
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello World")
```

### Adding More Functions ➕

Create additional functions in `views.py` as needed.

## Setting Up URLs 🔗

URLs are entry points to your views.

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

Templates and static files are essential for rendering HTML and serving CSS, JavaScript, and images.

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
    list_display = ('name', 'image')
    search_fields = ('name', 'image')

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

Use Django's template language to loop through and display data:

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
<small>Published on: {{ blog.published _date }}</small>
{% endfor %}
```

## Implementing Relationships 🔗

Create relationships between models using ForeignKey and ManyToManyField.

### Example: Adding a ForeignKey Relationship 📚

```python
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### Example: Adding a ManyToManyField 📚

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)
    blogs = models.ManyToManyField(Blog, related_name='tags')
```

## Django Forms 📝

Forms handle user input and validation.

### Creating a Form Class 📋

1. **Define a Form in `forms.py`:**

   ```python
   from django import forms
   from .models import UserDetails

   class UserForm(forms.ModelForm):
       class Meta:
           model = UserDetails
           fields = ['name', 'image']
   ```

2. **Use the Form in Views:**

   ```python
   from .forms import UserForm

   def create_user(request):
       if request.method == 'POST':
           form = UserForm(request.POST, request.FILES)
           if form.is_valid():
               form.save()
               return redirect('user_list')
       else:
           form = UserForm()
       return render(request, 'user_form.html', {'form': form})
   ```

3. **Display the Form in Templates:**

   ```html
   <form method="post" enctype="multipart/form-data">
     {% csrf_token %} {{ form.as_p }}
     <button type="submit">Submit</button>
   </form>
   ```

## Working with URL Parameters 🔍

Handle dynamic URLs and pass parameters to views.

### Example: Handling URL Parameters 🌐

1. **Define URL Pattern with Parameter:**

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('user/<int:id>/', views.user_detail, name='user_detail'),
   ]
   ```

2. **Create View Function to Handle Parameter:**

   ```python
   def user_detail(request, id):
       user = UserDetails.objects.get(id=id)
       return render(request, 'user_detail.html', {'user': user})
   ```

3. **Use Parameter in Template:**

   ```html
   <h1>{{ user.name }}</h1>
   <img src="{{ user.image.url }}" alt="{{ user.name }}" />
   ```

## Customizing the User Model 👤

Customize Django’s built-in User model to fit your needs.

### Extending the User Model with a Profile 🛠️

1. **Create a Profile Model:**

   ```python
   from django.contrib.auth.models import User
   from django.db import models

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       bio = models.TextField()
   ```

2. **Create a Signal to Automatically Create a Profile:**

   ```python
   from django.db.models.signals import post_save
   from django.dispatch import receiver

   @receiver(post_save, sender=User)
   def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(user=instance)
   ```

3. **Update the User Model in Forms and Views:**

   ```python
   from django import forms
   from django.contrib.auth.models import User
   from .models import Profile

   class UserProfileForm(forms.ModelForm):
       class Meta:
           model = Profile
           fields = ['bio']
   ```

## Adding Update and Delete Functionality 🔄

Implement the ability to update and delete records.

### Updating Records 🖋️

1. **Create a View to Handle Updates:**

   ```python
   def update_user(request, id):
       user = UserDetails.objects.get(id=id)
       if request.method == 'POST':
           form = UserForm(request.POST, request.FILES, instance=user)
           if form.is_valid():
               form.save()
               return redirect('user_list')
       else:
           form = UserForm(instance=user)
       return render(request, 'user_form.html', {'form': form})
   ```

2. **Update the URL Pattern:**

   ```python
   path('user/update/<int:id>/', views.update_user, name='update_user'),
   ```

### Deleting Records 🗑️

1. **Create a View to Handle Deletion:**

   ```python
   def delete_user(request, id):
       user = UserDetails.objects.get(id=id)
       if request.method == 'POST':
           user.delete()
           return redirect('user_list')
       return render(request, 'confirm_delete.html', {'user': user})
   ```

2. **Update the URL Pattern:**

   ```python
   path('user/delete/<int:id>/', views.delete_user, name='delete_user'),
   ```

## Adding Pagination 📜

Pagination splits large datasets into smaller pages for better usability.

### Implementing Pagination in Views 📚

1. **Update Your View Function:**

   ```python
   from django.core.paginator import Paginator

   def user_list(request):
       user_list = UserDetails.objects.all()
       paginator = Paginator(user_list, 10)  # Show 10 users per page
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)
       return render(request, 'user_list.html', {'page_obj': page_obj})
   ```

2. **Update Your Template:**

   ```html
   {% for user in page_obj %}
   <p>{{ user.name }}</p>
   {% endfor %}

   <div class="pagination">
     <span class="step-links">
       {% if page_obj.has_previous %}
       <a href="?page=1">&laquo; first</a>
       <a href="?page={{ page_obj.previous_page_number }}">previous</a>
       {% endif %}

       <span class="current">
         Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
       </span>

       {% if page_obj.has_next %}
       <a href="?page={{ page_obj.next_page_number }}">next</a>
       <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
       {% endif %}
     </span>
   </div>
   ```

### Example: Adding Pagination to Blog Posts 📄

```python
def blog_list(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 5)  # Show 5 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj})
```

```html
<!-- blog_list.html -->
{% for blog in page_obj %}
<h2>{{ blog.title }}</h2>
<p>{{ blog.content }}</p>
<small>Published on: {{ blog.published_date }}</small>
{% endfor %}

<div class="pagination">
  <span class="step-links">
    {% if page_obj.has_previous %}
    <a href="?page=1">&laquo; first</a>
    <a href="?page={{ page_obj.previous_page_number }}">previous</a>
    {% endif %}

    <span class="current">
      Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
    </span>

    {% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">next</a>
    <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
    {% endif %}
  </span>
</div>
```

## Adding Search Functionality 🔍

Search functionality enables users to find specific items quickly.

### Implementing Search in Views 🔎

1. **Update Your View Function:**

   ```python
   from django.db.models import Q

   def user_list(request):
       query = request.GET.get('q')
       if query:
           user_list = UserDetails.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
       else:
           user_list = UserDetails.objects.all()

       paginator = Paginator(user_list, 10)
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)
       return render(request, 'user_list.html', {'page_obj': page_obj, 'query': query})
   ```

2. **Update Your Template:**

   ```html
   <form method="get" action="{% url 'user_list' %}">
       <input type="text" name="q" value="{{ query }}" placeholder="Search users...">
       <button type="submit">Search</button>
   </form>

   {% for user in page_obj %}
   <p>{{ user.name }}</p>
   {% endfor %}

   <div class="pagination">
       <span class="step-links">
           {% if page_obj.has_previous %}
               <a href="?page=1&q={{ query }}">&laquo; first</a>
               <a href="?page={{ page_obj.previous_page_number }}&q={{ query }}">previous</a>
           {% endif %}

           <span class="current">
               Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
           </span>

           {% if page_obj.has_next %}
               <a href="?page={{ page_obj.next_page_number }}&q={{ query }}">next</a>
               <a href="?page={{ page_obj.paginator.num_pages }}&q={{ query }}">last &raquo;</a>
           {% endif %}
       </
   ```

span>

   </div>
   ```

### Example: Adding Search to Blog Posts 🔍

```python
def blog_list(request):
    query = request.GET.get('q')
    if query:
        blog_list = Blog.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        blog_list = Blog.objects.all()

    paginator = Paginator(blog_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj, 'query': query})
```

```html
<!-- blog_list.html -->
<form method="get" action="{% url 'blog_list' %}">
  <input
    type="text"
    name="q"
    value="{{ query }}"
    placeholder="Search blogs..."
  />
  <button type="submit">Search</button>
</form>

{% for blog in page_obj %}
<h2>{{ blog.title }}</h2>
<p>{{ blog.content }}</p>
<small>Published on: {{ blog.published_date }}</small>
{% endfor %}

<div class="pagination">
  <span class="step-links">
    {% if page_obj.has_previous %}
    <a href="?page=1&q={{ query }}">&laquo; first</a>
    <a href="?page={{ page_obj.previous_page_number }}&q={{ query }}"
      >previous</a
    >
    {% endif %}

    <span class="current">
      Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
    </span>

    {% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}&q={{ query }}">next</a>
    <a href="?page={{ page_obj.paginator.num_pages }}&q={{ query }}"
      >last &raquo;</a
    >
    {% endif %}
  </span>
</div>
```

## Conclusion 🎉

Congratulations! You've built a complete CRUD application with Django, including features like pagination and search functionality. Continue to explore Django's extensive documentation and community resources to enhance your skills and build more complex applications.

Happy coding! 🖥️🚀

---

Feel free to adjust any parts to better suit your audience or specific requirements!
