from django.http import JsonResponse
import requests
import datetime


def index(request):
    dt = datetime.datetime.today()
    
    if is_prime(dt.day):
        responseData = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=aa755402416ed58bb3d4613e43c7137e').json()
    else:
        responseData = "Date is not prime so no data"
    return JsonResponse({"data": responseData})


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            return True
    else:
        return False
