from django.urls import path

from .views import IndexView, MessageCreateView, SubscribeCreateView


app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('message/', MessageCreateView.as_view(), name='create-message'),
    path('subscribe/', SubscribeCreateView.as_view(), name='subscribe')
]