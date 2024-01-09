from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from .models import Qualifying, Driver, Final, Point

def index(request):
    return HttpResponse("f1")

def get_data(request):
    # Qualifyingデータを取得
    qualifying_data = Qualifying.objects.all()
    final_data = Final.objects.all()
    driver_data = Driver.objects.all()
    point_data = Point.objects.all()


    # Qualifyingデータとそれに関連するDriverデータをJSONに整形
    data = {
        'qualifying': [
            {
                'year': q.year,
                'gp': q.gp,
                'rank': q.rank,
                'driver': {
                    'name': q.driver.driver_name,
                }
            }
            for q in qualifying_data
        ],
        'drivers': [
            driver_to_dict(d)
            for d in driver_data
        ],

        'final': [
            {
                'year': q.year,
                'gp': q.gp,
                'rank': q.rank,
                'driver': {
                    'name': q.driver.driver_name,
                }
            }
            for q in final_data
        ],

        'point': [
            {
                'year': q.year,
                'point': q.point,
                'rank': q.rank,
                'driver': {
                    'name': q.driver.driver_name,
                }
            }
            for q in point_data
        ],
    }

    return JsonResponse(data)

def driver_to_dict(driver):
    return {
        'driver_name': driver.driver_name,
        'age': driver.age,
        'birthplace': driver.birthplace,
        'team': driver.team,
        'profile_picture': driver.profile_picture.url if driver.profile_picture else None,
    }