from django.shortcuts import render


def index(request):
    names = ["Mina", "Mark", "Bianca", "Marsilinou"]
    items = {"Rice": 4.25, "Milk": 7.37, "Egg": 5.99}
    # map = {}
    return render(request, 'index.html', {"names": names, "items": items})
