from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dash'),


]




# path   网站的前缀
