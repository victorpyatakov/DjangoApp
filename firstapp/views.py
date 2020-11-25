from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h2>О сайте</h2>")


def products(request, product_id=1):
    output = "<h2>Product # {0}</h2>".format(product_id)
    return HttpResponse(output)


def users(request, id=1, name='Victor'):
    output = "<h2>User</h2><h3>id: {0} name {1}</h3>".format(id, name)
    return HttpResponse(output)
