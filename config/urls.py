from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # ==========================================
    # Grappelli
    # ==========================================

    path(
        "grappelli/",
        include("grappelli.urls"),
    ),

    # ==========================================
    # Django Admin
    # ==========================================

    path(
        "admin/",
        admin.site.urls,
    ),

    # ==========================================
    # Admin AJAX APIs
    # ==========================================

    path(
        "admin/ajax/",
        include("apps.utility.admin.urls"),
    ),

    # ==========================================
    # About / Frontend
    # ==========================================

    path(
        "",
        include("apps.core.urls"),
    ),

    # ==========================================
    # Dashboard
    # ==========================================

    path(
        "",
        include("apps.dashboard.urls"),
    ),

    # ==========================================
    # Jobs
    # ==========================================

    path(
        "jobs/",
        include("apps.job.urls"),
    ),

    # ==========================================
    # Companies
    # ==========================================

    path(
        "companies/",
        include("apps.companies.urls"),
    ),

    # ==========================================
    # CKEditor
    # ==========================================

    path(
        "ckeditor5/",
        include("django_ckeditor_5.urls"),
    ),

    # ==========================================
    # Importer
    # ==========================================

    path(
        "importer/",
        include("apps.importer.urls"),
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )