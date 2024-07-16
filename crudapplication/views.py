from django.shortcuts import render
from .models import UserDetails
from .forms import ProductForm


def index(request):
    userDetails = UserDetails.objects.all()
    return render(request, "crudapplication/index.html", {"userDetails": userDetails})


def productForm(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, "crudapplication/product.html", {"form": form})
