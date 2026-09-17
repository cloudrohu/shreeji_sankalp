from django.shortcuts import render,redirect
from apps.core.models import Setting , Slider , About , Why_Choose , USP, PriceBreakupInquiry,Inquiry
from apps.properties.models import Project


def dashboard(request):

    settings_obj = Setting.objects.first()
    project_obj = Project.objects.first()

    if request.method == "POST":

        inquiry_type = request.POST.get("inquiry_type")

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if inquiry_type == "price_breakup":

            property_type = request.POST.get("property_type")
            property_area = request.POST.get("property_area")
            property_price = request.POST.get("property_price")

            if name and phone:

                PriceBreakupInquiry.objects.create(
                    project=project_obj,
                    name=name,
                    email=email,
                    phone=phone,
                    message=message,
                    property_type=property_type,
                    property_area=property_area,
                    property_price=property_price,
                )

                return redirect("thank_you")

        # =========================
        # VIRTUAL TOUR
        # =========================
        elif inquiry_type == "virtual_tour":

            if name and phone:

                Inquiry.objects.create(
                    project=project_obj,
                    name=name,
                    email=email,
                    phone=phone,
                    message="Virtual Tour Request",
                )

                return redirect("thank_you")

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

