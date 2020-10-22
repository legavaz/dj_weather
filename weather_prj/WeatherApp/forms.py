from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        atribute = {
            'class':'form-control',
            'name':"city",
            'id':"city",
            'placeholder':"Введите город"
            }
        # Добавляем теги/атрибуты в поле
        widgets = {'name':TextInput(attrs=atribute)}
        