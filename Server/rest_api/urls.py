from rest_api import views
from django.conf.urls import url

urlpatterns = [

    url(r'^read', views.read , name='read'),
    url(r'^delete', views.delete , name='delete'),
    url(r'^edit', views.edit , name='edit'),
    url(r'^create', views.create , name='create'),
]