from django.shortcuts import render,redirect

from apps.core.models.website import Setting,About,FAQ

from apps.properties.models import Project, Connectivity

# Create your views here.

def get_settings():
    """Helper function to fetch settings object safely"""
    return Setting.objects.first()

def about(request):
    settings_obj = get_settings()
    about_obj = About.objects.filter(setting=settings_obj).first()


    return render(
        request,
        'home/about.html',
        {
            'settings_obj': settings_obj,
            'about_obj': about_obj,

        }
    )

def FAQs(request):
    settings_obj = get_settings()
    about_obj = About.objects.filter(setting=settings_obj).first()

    faqs = FAQ.objects.filter(setting=settings_obj)


    return render(
        request,
        'home/faqs.html',
        {
            'settings_obj': settings_obj,
            'about_obj': about_obj,
            'faqs': faqs,

        }
    )


def Privacy_Policy(request):
  
    return render(request, 'home/privacy_policy.html', {'settings_obj': get_settings()})


def Disclaimer(request):
  
    return render(request, 'home/disclaimer.html', {'settings_obj': get_settings()})


def Amenities(request):
  
    return render(request, 'home/amenities.html', {'settings_obj': get_settings()})

def Location(request):
    settings_obj = get_settings()
    
    project_obj = Project.objects.first()
    
    connectivities = Connectivity.objects.filter(project=project_obj)

    return render(
        request,
        'home/Location.html',
        {
            'settings_obj': settings_obj,
            'project_obj': project_obj,
            'connectivities': connectivities,  # <-- Ye zaroori tha
        }
    )
def Floor_plans(request):
  
    return render(request, 'home/floor_plans.html', {'settings_obj': get_settings()})
    
def Gallery(request):
  
    return render(request, 'home/gallery.html', {'settings_obj': get_settings()})

    
def Contact(request):
  
    return render(request, 'home/contact.html', {'settings_obj': get_settings()})