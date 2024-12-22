from django.urls import path
from .views import home, brands_by_id, detail_cars, add_brand, add_car

urlpatterns = [
    path('', home, name="home"),
    path('brand/<int:brand_id>/', brands_by_id, name="brands_by_id"),
    path('cars/<int:detailed_car_id>/', detail_cars, name="detail_cars"),
    path('brand/add/', add_brand, name='add_brand'),
    path('cars/add/', add_car, name='add_car'),
]


