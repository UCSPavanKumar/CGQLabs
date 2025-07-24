from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    #path('sendsms/<str:content>/<str:phone_number>/', views.sendsms, name='sendsms'),
    path('api/', views.api_page, name='api_page'),
    path('automation/', views.automation_page, name='automation_page'),
    path('finance/', views.finance_page, name='finance_page'),
    path('contact/', views.contact_us, name='contact_us'),
    path('submit_contact/', views.submit_contact_form, name='submit_contact_form'),
    path('management/', views.management, name='management'),
]

