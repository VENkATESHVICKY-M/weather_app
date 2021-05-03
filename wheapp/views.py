from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import urllib.request

def base(request):
    if request.method == "POST":
        city = request.POST['city']
        """api key"""
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()
        print("1-----------------------------")
        print(source)
        list_of_data = json.loads(source)
        

        print("-=====================")
        print(list_of_data)
        context = {
               "name": str(list_of_data['name']),
                "country": str(list_of_data['sys']['country']) ,
                "temp": str(int(list_of_data['main']['temp']-273)) + '*C',
                "feels_like": str(int(list_of_data['main']['feels_like']-273)) + '*C',
                "weather": str(list_of_data['weather'][0]['main']),}
        print("2------------------------------")
        print(context)
    else:
        context={}
    
    return render(request,'base.html', context)

