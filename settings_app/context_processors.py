from .models import SeoSettings, SiteSettings, SocialNetworks

def settings_processor(request):
    seo_settings = SeoSettings.objects.last()
    site_settings = SiteSettings.objects.last()
    social_networks = SocialNetworks.objects.all()


    return {
        'seo_settings': seo_settings,
        'site_settings': site_settings,
        'social_networks': social_networks,
    }
