from django.shortcuts import render
from .forms import UserFrom
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        user_form = UserFrom()
        return render(request, "index.html",{"form":user_form})

