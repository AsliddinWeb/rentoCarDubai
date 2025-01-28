from django.urls import path

from .views import news_page, news_category_page, news_detail_page

urlpatterns = [
    path('', news_page, name='news_page'),
    path('<int:pk>/', news_category_page, name='news_category_page'),

    path('detail/<int:pk>/', news_detail_page, name='news_detail_page'),
]
