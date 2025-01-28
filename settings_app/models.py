from django.db import models

class SeoSettings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sayt nomi")
    favicon = models.FileField(upload_to='favicons/', verbose_name="Favicon")

    site_author = models.TextField(verbose_name="Sayt muallifi")
    site_keywords = models.TextField(verbose_name="Sayt kalit so‘zlari")
    site_description = models.TextField(verbose_name="Sayt tavsifi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "SEO Sozlamalari"
        verbose_name_plural = "SEO Sozlamalari"

class SiteSettings(models.Model):
    phone_number = models.CharField(max_length=255, verbose_name="Telefon raqami")

    whatsapp_phone = models.CharField(max_length=255, verbose_name="WhatsApp telefon raqami")
    telegram_phone = models.CharField(max_length=255, verbose_name="Telegram telefon raqami")
    telegram_username = models.CharField(max_length=255, verbose_name="Telegram foydalanuvchi nomi")

    email = models.CharField(max_length=255, null=True, blank=True, verbose_name="Email")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Manzil")

    header_logo = models.ImageField(upload_to='logos/', verbose_name="Bosh logo")
    footer_logo = models.ImageField(upload_to='logos/', verbose_name="Pastki logo")

    footer_text = models.TextField(verbose_name="Pastki matn")
    copyright_text = models.TextField(verbose_name="Mualliflik huquqi matni")

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Sayt Sozlamalari"
        verbose_name_plural = "Sayt Sozlamalari"

class SocialNetworks(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ijtimoiy tarmoq nomi")
    icon = models.CharField(max_length=255, verbose_name="Ijtimoiy tarmoq ikonkasi")
    link = models.CharField(max_length=255, verbose_name="Ijtimoiy tarmoq havolasi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ijtimoiy Tarmoq"
        verbose_name_plural = "Ijtimoiy Tarmoqlar"

class TelegramBotConfig(models.Model):
    username = models.CharField(max_length=255, verbose_name="Bot foydalanuvchi nomi")
    token = models.TextField(verbose_name="Bot tokeni")
    admins = models.CharField(max_length=255, verbose_name="Adminlar")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Telegram Bot Konfiguratsiyasi"
        verbose_name_plural = "Telegram Bot Konfiguratsiyalari"
