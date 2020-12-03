from django.shortcuts import render
# Create your views here.


def index(request):
    header = "Personal Data"
    langs = ["English", 'Spanish', 'German']
    user = {'name': 'Victor', 'age': '25'}
    address = ('Абрикосовая', 23, 45)

    data = {"header": header, 'language': langs, 'user': user, 'address': address, 'n': 5}
    return render(request, "index.html", context=data)
