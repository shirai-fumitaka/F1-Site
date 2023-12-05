from django.urls import path
from . import views
from .views import get_data

urlpatterns = [
   path('', views.index, name='index'),
   path('api/data/', views.get_data, name='api_data'),
]