from django.shortcuts import render,redirect

from apps.core.models.website import Setting


# Create your views here.

def get_settings():
    """Helper function to fetch settings object safely"""
    return Setting.objects.first()

def about(request):
  
    return render(request, 'home/about.html', {'settings_obj': get_settings()})

def FAQs(request):
  
    return render(request, 'home/faqs.html', {'settings_obj': get_settings()})


def Privacy_Policy(request):
  
    return render(request, 'home/privacy_policy.html', {'settings_obj': get_settings()})


def Disclaimer(request):
  
    return render(request, 'home/disclaimer.html', {'settings_obj': get_settings()})


def Amenities(request):
  
    return render(request, 'home/amenities.html', {'settings_obj': get_settings()})

    
def Location(request):
  
    return render(request, 'home/location.html', {'settings_obj': get_settings()})

def Floor_plans(request):
  
    return render(request, 'home/floor_plans.html', {'settings_obj': get_settings()})
    
def Gallery(request):
  
    return render(request, 'home/gallery.html', {'settings_obj': get_settings()})

    
def Contact(request):
  
    return render(request, 'home/contact.html', {'settings_obj': get_settings()})