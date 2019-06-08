from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
import json


def index(request):

    return render(request, 'test.html')

def get_data(request):

    print(request.method)
    print(type(request.GET))
    print(request.GET)
    if request.method == 'POST':
        print("hello")
        JSON_load = json.loads(request.GET)
        print(JSON_load)

    return HttpResponse('hleo')
