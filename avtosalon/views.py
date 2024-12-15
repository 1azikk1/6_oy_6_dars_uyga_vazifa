from django.shortcuts import render
from .models import Brand, Car


def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.filter(is_available=True)
    context = {
        'brands': brands,
        'cars': cars
    }
    return render(request, 'index.html', context)


def brands_by_id(request, brand_id):
    brands = Brand.objects.all()
    cars = Car.objects.filter(brand_id=brand_id, is_available=True)
    context = {
        'brands': brands,
        'cars': cars
    }
    return render(request, 'index.html', context)


def detail_cars(request, detailed_car_id):
    car = Car.objects.get(id=detailed_car_id, is_available=True)
    car.views += 1
    car.save()
    return render(request, 'detail.html', {'car': car})
