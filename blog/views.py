from django.shortcuts import render
from django.http import HttpResponse
from .models import blog
# Create your views here.
def index(request):
    b = blog.objects.all() 
    context={
        "title":"AYAN BLOG"
        "post": b
    }
    