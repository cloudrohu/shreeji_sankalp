from django.shortcuts import render, redirect

from apps.core.models.website import Setting, About, FAQ, Inquiry, PriceBreakupInquiry, Why_Choose, USP, Slider
from apps.properties.models import Project, Connectivity, ProjectAmenities, Gallery

def get_common_context(extra_context=None):
   
    settings_obj = Setting.objects.first()
    all_projects = Project.objects.all().order_by('id')

    project_obj = Project.objects.filter(id=1, is_active=True, featured_property=True).first()
    if not project_obj:
        project_obj = Project.objects.filter(
            is_active=True, 
            featured_property=True
        ).first() or Project.objects.filter(is_active=True).first()

    context = {
        'settings_obj': settings_obj,
        'all_projects': all_projects,
        'project_obj': project_obj,
    }

    if extra_context:
        context.update(extra_context)

    return context

def dashboard(request):
    settings_obj = Setting.objects.first()

    project_obj = Project.objects.filter(id=1, is_active=True, featured_property=True).first()
    if not project_obj:
        project_obj = Project.objects.filter(
            is_active=True, 
            featured_property=True
        ).first() or Project.objects.filter(is_active=True).first()

    if request.method == "POST":
        inquiry_type = request.POST.get("inquiry_type")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if inquiry_type == "price_breakup" and name and phone:
            property_type = request.POST.get("property_type")
            property_area = request.POST.get("property_area")
            property_price = request.POST.get("property_price")

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

        elif inquiry_type == "virtual_tour" and name and phone:
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
        get_common_context({
            "slider": slider,
            "about_obj": about_obj,
            "why_choose": why_choose,
            "unique_selling_proposition": unique_selling_proposition,
        })
    )


def about(request):
    settings_obj = Setting.objects.first()
    about_obj = About.objects.filter(setting=settings_obj).first()

    return render(
        request,
        'home/about.html',
        get_common_context({
            'about_obj': about_obj,
        })
    )


def FAQs(request):
    settings_obj = Setting.objects.first()
    about_obj = About.objects.filter(setting=settings_obj).first()
    faqs = FAQ.objects.filter(setting=settings_obj)

    return render(
        request,
        'home/faqs.html',
        get_common_context({
            'about_obj': about_obj,
            'faqs': faqs,
        })
    )


def Privacy_Policy(request):
    return render(request, 'home/privacy_policy.html', get_common_context())


def Disclaimer(request):
    return render(request, 'home/disclaimer.html', get_common_context())


def Amenities(request):
    amenities = ProjectAmenities.objects.all()
    return render(
        request, 
        'home/amenities.html', 
        get_common_context({
            'amenities': amenities,
        })
    )


def Location(request):
    context = get_common_context()
    project_obj = context['project_obj']

    connectivities = Connectivity.objects.filter(project=project_obj)
    context.update({'connectivities': connectivities})

    return render(request, 'home/location.html', context)


def Floor_plans(request):
    return render(request, 'home/floor_plans.html', get_common_context())


def GalleryView(request):
    context = get_common_context()
    project_obj = context['project_obj']

    gallery_items = Gallery.objects.filter(project=project_obj)
    context.update({'gallery_items': gallery_items})

    return render(request, 'home/gallery.html', context)


def ContactView(request):
    context = get_common_context()
    project_obj = context['project_obj']

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if name and phone:
            Inquiry.objects.create(
                project=project_obj,
                name=name,
                email=email,
                phone=phone,
                message=message,
            )
            return redirect('thank_you')

    return render(request, 'home/contact.html', context)


def ThankYouView(request):
    return render(request, 'home/thank_you.html', get_common_context())

def Developer(request):
    return render(request, 'home/developer.html', get_common_context())