from django.urls import path

from .views import index, calendario

urlpatterns = [
    path("", index, name="index"),
    path('calendario/<int:ano>/<int:mes>/', calendario, name='calendario'),
]