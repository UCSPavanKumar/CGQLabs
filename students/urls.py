from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sendsms/<str:content>/<str:phone_number>/', views.sendsms, name='sendsms'),
]

