from django.db import models

class CarCosiness(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='cosinesses', verbose_name="Avtomobil")
    title = models.CharField(max_length=255, verbose_name="Qulaylik nomi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Avtomobil qulayligi"
        verbose_name_plural = "Avtomobil qulayliklari"


class CarImage(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='images', verbose_name="Avtomobil")
    title = models.CharField(max_length=255, verbose_name="Rasm nomi")
    image = models.ImageField(upload_to='car-images/', verbose_name="Rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Avtomobil rasmi"
        verbose_name_plural = "Avtomobil rasmlari"


class CarCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Tavsif")
    image = models.ImageField(upload_to='car_categories/', verbose_name="Rasm")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Avtomobil kategoriyasi"
        verbose_name_plural = "Avtomobil kategoriyalari"


class CarType(models.Model):
    title = models.CharField(max_length=255, verbose_name="Nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Tavsif")
    image = models.ImageField(upload_to='car_types/', verbose_name="Rasm")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Avtomobil turi"
        verbose_name_plural = "Avtomobil turlari"


class CarBrand(models.Model):
    title = models.CharField(max_length=255, verbose_name="Brend nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Tavsif")
    image = models.ImageField(upload_to='car_brands/', verbose_name="Rasm")
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name="Link")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Avtomobil brendi"
        verbose_name_plural = "Avtomobil brendlari"


class Car(models.Model):
    title = models.CharField(max_length=255, verbose_name="Avtomobil nomi")
    description = models.TextField(verbose_name="Tavsif")
    main_image = models.ImageField(upload_to='cars/', verbose_name="Asosiy rasm")

    car_category = models.ForeignKey(CarCategory, on_delete=models.PROTECT, verbose_name="Kategoriya")
    car_type = models.ForeignKey(CarType, on_delete=models.PROTECT, verbose_name="Turi")
    car_brand = models.ForeignKey(CarBrand, on_delete=models.PROTECT, verbose_name="Brend")

    doors = models.CharField(max_length=255, verbose_name="Eshiklar")
    passengers = models.CharField(max_length=255, verbose_name="Yolovchilar")
    transmission = models.CharField(max_length=255, default='Auto', verbose_name="Uzatma")
    luggage = models.CharField(max_length=255, verbose_name="Bagaj")

    one_day_price = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bir kunlik narx")
    one_week_price = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bir haftalik narx")
    one_month_price = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bir oylik narx")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Avtomobil"
        verbose_name_plural = "Avtomobillar"
        ordering = ['-id']
