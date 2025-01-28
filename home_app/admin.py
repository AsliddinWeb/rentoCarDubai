from django.contrib import admin
from .models import About, PromoVideo, ClientFeedback, Booking, ContactPage, Message

# Unfold admin
from unfold.admin import ModelAdmin

@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ('id', 'title', 'cap_title', 'button_link')
    search_fields = ('title', 'cap_title', 'description')
    list_filter = ('title',)

@admin.register(PromoVideo)
class PromoVideoAdmin(ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(ClientFeedback)
class ClientFeedbackAdmin(ModelAdmin):
    list_display = ('id', 'name', 'who', 'rating')
    search_fields = ('name', 'who', 'feedback')
    list_filter = ('rating',)

@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'car_type', 'pick_up_date', 'return_date', 'created_at')
    list_filter = ('car_type', 'pick_up_date', 'return_date', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'car_type', 'pick_up_location', 'drop_off_location')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'


@admin.register(ContactPage)
class ContactPageAdmin(ModelAdmin):
    list_display = ('email', 'address', 'opening_hours', 'phone_number')
    search_fields = ('email', 'address', 'phone_number')

@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'subject', 'is_checked', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('is_checked', 'created_at')
