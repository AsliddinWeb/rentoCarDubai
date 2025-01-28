from .models import CarType, CarBrand

def car_processor(request):
    car_types = CarType.objects.all()
    car_brands = CarBrand.objects.all()


    return {
        'car_types': car_types,
        'car_brands': car_brands,
    }
