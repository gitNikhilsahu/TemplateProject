from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.MyTempView),
    path('wish/', views.Welcome_Page),
    path('thank/', views.Thanks_Page),
]
