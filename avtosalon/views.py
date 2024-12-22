from django.shortcuts import render
from .models import Brand, Car
from .forms import BrandForm, CarForm


def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.filter(is_available=True)
    context = {
        'brands': brands,
        'cars': cars,
        'title': 'Find the perfect drive'
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


def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            brands = Brand.objects.create(**form.cleaned_data)
            print(brands, "qo'shildi!")

    brands = BrandForm()
    context = {
        'title': 'Add brand',
        'form': brands
    }
    return render(request, 'add_brand.html', context)


def add_car(request):
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            cars = Car.objects.create(**form.cleaned_data)
            print(cars, "qo'shildi!")

    cars = CarForm()
    context = {
        'title': 'Add car',
        'form': cars
    }
    return render(request, 'add_car.html', context)
