from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('api/dashboard', views.api_dashboard, name='dashboard_apis'),
]
# path   网站的前缀
