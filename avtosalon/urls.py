from django.urls import path
from .views import home, brands_by_id, detail_cars

urlpatterns = [
    path('', home, name="home"),
    path('brand/<int:brand_id>/', brands_by_id, name="brands_by_id"),
    path('cars/<int:detailed_car_id>/', detail_cars, name="detail_cars"),
]


