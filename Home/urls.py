from Home import views
from django.conf import settings
from django.urls import include,path

urlpatterns = [
    path('',views.index,name='Home'),
    path('contact',views.contact,name='contact'),
]