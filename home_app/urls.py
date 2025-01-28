from django.urls import path

from .views import (home_page, about_page, booking_create, car_types_page,
                    car_type_cars_page, all_cars_page, contact_page, car_brands_page, brand_cars_page)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('car-types/', car_types_page, name='car_types_page'),
    path('car-types/<int:pk>/', car_type_cars_page, name='car_type_cars_page'),
    path('cars/', all_cars_page, name='all_cars_page'),
    path('brands/', car_brands_page, name='car_brands_page'),
    path('brands/<int:pk>/', brand_cars_page, name='brand_cars_page'),

    path('contact/', contact_page, name='contact_page'),

    # Booking
    path('booking/', booking_create, name='booking_create'),
]
