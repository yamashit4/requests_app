from django.shortcuts import render
import requests

url = "https://weather.tsukumijima.net/"

# Create your views here.

def index(request):
    context = {'message': "Welcome my REQUESTS",}
    return render(request, 'request/index.html',context)

def get_weather_data(request):
    return render(request, 'request/weather.html')