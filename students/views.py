from django.shortcuts import render
from twilio.rest import Client
from django.http import HttpResponse
from dotenv import load_dotenv
load_dotenv()
import os
# Create your views here.
def index(request):
    return render(request, 'students/index.html')

