from django.shortcuts import render
from django.http import HttpResponse
from .models import Qualifying 
from django.http import JsonResponse


def index(request):
    return HttpResponse("f1")

def get_data (request):
    qualifying_data= Qualifying.objects.all()
    data ={'qualifying':[{'id':q.id,'venue':q.venue,'rank':q.rank,'driver_name':q.driver_name} for q in qualifying_data]}
    return JsonResponse(data)

# Create your views here.
