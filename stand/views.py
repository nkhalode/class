from django.shortcuts import render
from stand.models import BlogApp

# Create your views here.

def BlogView(request):

    blog = BlogApp.objects.all()

    return render(request,'stand/index.html',{'nilesh':blog})
