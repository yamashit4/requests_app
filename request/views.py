from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    context = {'message': "Welcome my REQUESTS",}
    return render(request, 'request/index.html',context)

def get_weather_data(request):
    if request.method == 'POST':
        location = request.POST['location']

    param = {
            "city" : location
        }
    
    url = "https://weather.tsukumijima.net/api/forecast"
    response = requests.get(url,params=param)
    data =  response.json()

    today = data["forecasts"][0]
    date = "<" + today["date"] + ">"
    detail = (f'今日は{today["detail"]["weather"]}で、{today["detail"]["wind"]}の風')
    min_temperature = (f'最低気温は{today["temperature"]["min"]["celsius"]}℃')
    max_temperature = (f'最高気温は{today["temperature"]["max"]["celsius"]}℃')

    context = {
        "date": date,
        "detail" : detail,
        "min_temperature" : min_temperature,
        "max_temperature" : max_temperature,
    }

    return render(request, 'request/weather.html',context)