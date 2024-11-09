from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import Index,Nft,About_Us

urlpatterns = [
    path('',Index,name='Index'),
    path('nfts',Nft,name='nfts'),
    path('about-us',About_Us,name='about'),
]
