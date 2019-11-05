from django.shortcuts import render
from django.http import JsonResponse


def dashboard_page(request):
    return render(request, "dashboard/dashboard.html", {})


def api_dashboard(request):
    return JsonResponse({
         'avg_temperature': 20,
         'avg_pressure': 20,
         'avg_co2': 20,
         'avg_tvoc': 20,
         'avg_humidity': 20,
    })
