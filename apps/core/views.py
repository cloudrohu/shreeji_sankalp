from django.shortcuts import render,redirect

# Create your views here.

def about(request):
  
    return render(request, 'home/about.html',)