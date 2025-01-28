from django.contrib import admin
from .models import SeoSettings, SiteSettings, SocialNetworks, TelegramBotConfig

# Unfold
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

# Unfold auth app
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(SeoSettings)
class SeoSettingsAdmin(ModelAdmin):
    list_display = ('title', 'favicon', 'site_author', 'site_keywords', 'site_description')
    search_fields = ('title', 'site_author', 'site_keywords', 'site_description')

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ('phone_number', 'whatsapp_phone', 'telegram_phone', 'telegram_username', 'email', 'address')
    search_fields = ('phone_number', 'whatsapp_phone', 'telegram_phone', 'telegram_username', 'email', 'address')

@admin.register(SocialNetworks)
class SocialNetworksAdmin(ModelAdmin):
    list_display = ('title', 'icon', 'link')
    search_fields = ('title', 'icon', 'link')

@admin.register(TelegramBotConfig)
class TelegramBotConfigAdmin(ModelAdmin):
    list_display = ('username', 'token', 'admins')
    search_fields = ('username', 'admins')