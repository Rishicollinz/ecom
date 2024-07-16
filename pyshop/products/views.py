from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Offer


# Create your views here.
def index(req):
    prods = Product.objects.all()

    return render(req, 'products.html', {'products': prods})


def new_prod(req):
    return HttpResponse("New Products!", req)
