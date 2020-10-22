from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm



# Create your views here.
def index(request):

    API_ID = "ea0abb55f23e321f61804c8ded782330"
    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units=Metric&appid={1}"

    if request.method == "POST":
        form = CityForm(request.POST)
        print(request.POST)
        form.save()

    # Очистим форму    
    form = CityForm()
    

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        try:
            res = requests.get(url.format(city.name, API_ID)).json()
            city_info = {
                "city_name": city.name,
                "temp": res["main"]["temp"],
                "icon": res["weather"][0]["icon"],
            }
            all_cities.append(city_info)
        except:
            print("err-", city)

    context = {"all_info": all_cities, "form": form}

    if __name__ != "__main__":
        return render(request, "weather/index.html", context)


if __name__ == "__main__":
    index("test")
