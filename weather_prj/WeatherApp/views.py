from django.shortcuts import render
import requests 


# Create your views here.
def index(request):

    API_ID      =   'ea0abb55f23e321f61804c8ded782330'
    city_name   =   'Lipetsk'
    url         =   'https://api.openweathermap.org/data/2.5/weather?q={0}&units=Metric&appid={1}'

    res = requests.get(url.format(city_name,API_ID)).json()
    
    city_info   =   {
                    'city_name': city_name,
                    'temp':res['main']['temp'],
                    'icon':res['weather'][0]['icon'],
                    }
    
    context = {'info':city_info}
    # print (res)

    return render(request,'weather/index.html',context)


if __name__ == "__main__":
    index('test')

    