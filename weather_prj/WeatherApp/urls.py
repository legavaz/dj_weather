
from django.urls import path
from . import views             # импорт из текущей дериктории

urlpatterns = [    
    path('', views.index),
]