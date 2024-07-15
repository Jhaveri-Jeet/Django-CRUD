from django.shortcuts import render
from .models import UserDetails


def index(request):
    userDetails = UserDetails.objects.all()
    return render(request, "crudapplication/index.html", {'userDetails': userDetails})
