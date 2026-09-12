from django.shortcuts import render
from apps.core.models import Setting , Slider , About , Why_Choose , USP
from apps.properties.models import Project


def dashboard(request):

    settings_obj = Setting.objects.first()

    project_obj = Project.objects.first()

    about_obj = About.objects.filter(setting=settings_obj).first()

    why_choose = Why_Choose.objects.filter(setting=settings_obj).all()

    unique_selling_proposition = USP.objects.filter(setting=settings_obj).all()


    slider = (
        settings_obj.sliders.all()
        if settings_obj
        else Slider.objects.all()
    )

    return render(
        request,
        "home/index.html",
        {
            "settings_obj": settings_obj,
            "slider": slider,
            "project_obj": project_obj,
            "about_obj": about_obj,
            "why_choose": why_choose,
            "unique_selling_proposition": unique_selling_proposition,



        }
    )


