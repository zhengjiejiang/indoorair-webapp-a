from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dashoard'),
    path('api/dashboard',views.dashboard_api, name = 'dashboard_api'),


]

# path   网站的前缀
