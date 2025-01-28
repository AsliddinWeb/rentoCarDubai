import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt


from .models import About, PromoVideo, ClientFeedback, Booking, ContactPage, Message
from car_app.models import Car, CarType, CarBrand
from news_app.models import News

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'

def home_page(request):
    about = About.objects.last()
    promo_video = PromoVideo.objects.last()
    feedbacks = ClientFeedback.objects.all()

    news = News.objects.all()

    car_type = get_object_or_404(CarType, pk=1)

    luxury_cars = Car.objects.filter(car_type=car_type)

    ctx = {
        'about': about,
        'promo_video': promo_video,
        'feedbacks': feedbacks,

        'news': news,

        'luxury_cars': luxury_cars,
    }
    return render(request, 'home.html', ctx)

def about_page(request):
    about = About.objects.last()
    promo_video = PromoVideo.objects.last()

    ctx = {
        'about': about,
        'promo_video': promo_video,
    }

    return render(request, 'about.html', ctx)

def car_types_page(request):
    return render(request, 'car-types.html')

def car_type_cars_page(request, pk):
    car_type = get_object_or_404(CarType, pk=pk)
    cars = Car.objects.filter(car_type=car_type)

    paginator = Paginator(cars, 15)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    ctx = {
        'car_type': car_type,
        'page_obj': page_obj,
    }

    return render(request, 'car-type-cars.html', ctx)

def all_cars_page(request):
    cars = Car.objects.all()

    # Filtering logic
    search_query = request.GET.get('search', '')
    if search_query:
        cars = cars.filter(title__icontains=search_query)

    car_brand_id = request.GET.get('car_brand')
    if car_brand_id:
        cars = cars.filter(car_brand__id=car_brand_id)

    car_type_id = request.GET.get('car_type')
    if car_type_id:
        cars = cars.filter(car_type__id=car_type_id)

    transmission = request.GET.get('transmission')
    if transmission:
        cars = cars.filter(transmission=transmission)

    paginator = Paginator(cars, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'page_obj': page_obj,
    }

    return render(request, 'all-cars.html', ctx)



@csrf_exempt
def booking_create(request):
    if request.method == 'POST':
        print(request.POST)
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        car_type = request.POST.get('car_type')
        pick_up_location = request.POST.get('pick_up_location')
        pick_up_date = request.POST.get('pick_up_date')
        drop_off_location = request.POST.get('drop_off_location')
        return_date = request.POST.get('return_date')
        additional_note = request.POST.get('message')

        booking = Booking.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            car_type=car_type,
            pick_up_location=pick_up_location,
            pick_up_date=pick_up_date,
            drop_off_location=drop_off_location,
            return_date=return_date,
            additional_note=additional_note
        )

        message = (
            f"📋 **Yangi Bronlash:**\n\n"
            f"👤 Ism: {full_name}\n"
            f"📧 Email: {email}\n"
            f"📞 Telefon: {phone}\n"
            f"🚗 Avtomobil turi: {car_type}\n"
            f"📍 Pick Up joyi: {pick_up_location}\n"
            f"📅 Pick Up sanasi: {pick_up_date}\n"
            f"🏁 Drop Off joyi: {drop_off_location}\n"
            f"📅 Return sanasi: {return_date}\n"
            f"📝 Izoh: {additional_note}"
        )
        send_telegram_message(message)

        return redirect('home_page')
    return redirect('home_page')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, data=payload)

def contact_page(request):
    contact_data = ContactPage.objects.last()
    success_message = None

    if request.method == "POST":
        # Formdan ma'lumotlarni olish
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")
        message_content = request.POST.get("message")

        # Ma'lumotlarni saqlash
        new_message = Message.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            subject=subject,
            message=message_content,
        )

        # Telegramga xabar yuborish
        telegram_message = f"📩 Yangi Xabar:\n\n👤 Ism: {name}\n📧 Email: {email}\n📞 Telefon: {phone_number}\n📝 Mavzu: {subject}\n\n✉️ Xabar:\n{message_content}"
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(telegram_url, data={"chat_id": TELEGRAM_CHAT_ID, "text": telegram_message})

        # Muvaffaqiyat xabarini qaytarish
        success_message = "Your message was sent successfully."

    ctx = {
        "contact_data": contact_data,
        "success_message": success_message,
    }
    return render(request, "contact.html", ctx)

def car_brands_page(request):
    return render(request, 'car-brands.html')

def brand_cars_page(request, pk):
    car_brand = get_object_or_404(CarBrand, pk=pk)
    cars = Car.objects.filter(car_brand=car_brand)

    paginator = Paginator(cars, 15)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    ctx = {
        'car_brand': car_brand,
        'page_obj': page_obj,
    }

    return render(request, 'car-type-cars.html', ctx)
