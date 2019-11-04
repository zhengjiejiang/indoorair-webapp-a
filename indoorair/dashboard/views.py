from django.http import HttpResponse
from django.shortcuts import render


def dashboard_page(request):
  return render(request, "dashboard/dashboard.html",{},)

def dashboard_api(request):

  temp_avg = request.POST.get("temp_avg")
  press_avg = request.POST.get("press_avg")
  co2_avg = request.POST.get("co2_avg")
  tvoc_avg = request.POST.get("tvoc_avg")
  humid_avg = request.POST.get("humid_avg")
  # This is for debugging purposes only.

  return JsonResponse({
       "temp_avg": temp_avg,
       "press_avg": press_avg,
       "co2_avg": co2_avg,
       "tvoc_avg": tvoc_avg,
       "humid_avg": humid_avg,

  })
