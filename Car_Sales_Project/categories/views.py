from django.shortcuts import render
from .models import Brand
from cars.models import Car

# Create your views here.
def category_list(request):
    categories = Brand.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def filter_by_brand(request, brand_slug):
    brands = Brand.objects.all()

    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        cars = Car.objects.filter(brand=brand)
        context = {'brand': brand, 'cars': cars}
    else:
        context = {'brands': brands}

    return render(request, 'filter_by_brand.html', context)