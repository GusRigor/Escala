from django.urls import path

from .views import index, calendario, download_pdf

urlpatterns = [
    path("", index, name="index"),
    path('calendario/<int:ano>/<int:mes>/', calendario, name='calendario'),
    path('download-pdf/', download_pdf, name='download_pdf'),
]