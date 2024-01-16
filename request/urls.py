from django.urls import path
from . import views

app_name="request"

urlpatterns = [
  path('', views.index, name='index'),
  path('weather/',views.get_weather_data, name='weather')
]