from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h2>О сайте</h2>")


def products(request, product_id):
    category = request.GET.get("cat", "")
    output = "<h2>Product # {0} Category: {1}</h2>".format(product_id, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0} name {1}</h3>".format(id, name)
    return HttpResponse(output)
