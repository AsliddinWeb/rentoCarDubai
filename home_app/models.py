from django.db import models

from car_app.models import Car

class About(models.Model):
    cap_title = models.CharField(max_length=255, verbose_name="Bosh sarlavha")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")

    one_text = models.CharField(max_length=255, verbose_name="Birinchi matn")
    two_text = models.CharField(max_length=255, verbose_name="Ikkinchi matn")

    button_link = models.CharField(max_length=255, verbose_name="Tugma havolasi")

    image = models.ImageField(upload_to='about_pics/', verbose_name="Rasm")
    video = models.TextField(verbose_name="Video")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"

class PromoVideo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    video = models.TextField(verbose_name="Video")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Promo Video"
        verbose_name_plural = "Promo Videolar"

class ClientFeedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism")
    image = models.ImageField(upload_to='client_images/', null=True, blank=True, verbose_name="Rasm")
    who = models.CharField(max_length=255, verbose_name="Kimligi")
    feedback = models.TextField(verbose_name="Fikr")
    rating = models.IntegerField(default=5, verbose_name="Reyting")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Mijoz fikri"
        verbose_name_plural = "Mijoz fikrlari"

class Booking(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="To‘liq ismi")
    email = models.EmailField(verbose_name="Elektron pochta")
    phone = models.CharField(max_length=15, verbose_name="Telefon raqami")
    car_type = models.CharField(max_length=50, verbose_name="Avtomobil turi")
    pick_up_location = models.CharField(max_length=255, verbose_name="Jo‘nab ketish joyi")
    drop_off_location = models.CharField(max_length=255, verbose_name="Yetkazib berish joyi")
    pick_up_date = models.CharField(max_length=255, verbose_name="Jo‘nab ketish sanasi")
    return_date = models.CharField(max_length=255, verbose_name="Qaytish sanasi")
    additional_note = models.TextField(blank=True, null=True, verbose_name="Qo‘shimcha eslatma")

    is_checked = models.BooleanField(default=False, verbose_name="Tekshirildimi?")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"

    def __str__(self):
        return f"{self.full_name} - {self.car_type}"

class ContactPage(models.Model):
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    opening_hours = models.CharField(max_length=255, verbose_name="Ish vaqti")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami")
    google_maps_iframe = models.TextField(verbose_name="Google Maps iframe")

    class Meta:
        verbose_name = "Aloqa sahifasi"
        verbose_name_plural = "Aloqa sahifalari"

    def __str__(self):
        return f"Aloqa ma'lumotlari: {self.email}"

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami")
    subject = models.CharField(max_length=150, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar")

    is_checked = models.BooleanField(default=False, verbose_name="Tekshirildimi?")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return f"{self.name} - {self.subject}"

class HomeLuxuryCars(models.Model):
    title = models.CharField(max_length=255, verbose_name="Eng Top mashinalar")
    cars = models.ManyToManyField(Car, verbose_name="Mashinalar", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Eng Top mashina"
        verbose_name_plural = "Eng Top mashinalar"
