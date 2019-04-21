from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    if request.method == 'POST':
        data = dict(request.POST)
        print(data)
        d = [request.POST.get(str(x)) for x in range(20) if request.POST.get(str(x)) != None]
        # d = [request.POST.get(str(x)) for x in range(6) if request.POST.get(str(x)) != None]
        return HttpResponse(" ".join([str("%s\n"%x) for x in d]))

    names = ["Mina", "Mark", "Bianca", "Marsilinou"]
    items = {"Rice": 4.25, "Milk": 7.37, "Egg": 5.99}
    # map = {}
    return render(request, 'index.html', {"names": names, "items": items})


def hello(request):
    return HttpResponse('Hello World!')


def home(request):
    return render_to_response('in.html', {'variable': 'bo'})

def split(request):
    return render_to_response('split.html', {'names': names,
                                             "items":items})

