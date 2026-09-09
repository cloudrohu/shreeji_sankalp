from django.shortcuts import render
from apps.core.models import Setting , Slider


def dashboard(request):

    settings_obj = Setting.objects.first()

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
        }
    )

