from django.shortcuts import render
from twilio.rest import Client
from django.http import HttpResponse
from dotenv import load_dotenv
load_dotenv()
import os
# Create your views here.
def index(request):
    return render(request, 'students/index.html')

def sendsms(request,content,phone_number):
    """
    Send text sms using twilio SMS API
    """
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    print(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+18482799449',
    body=content,
    to=phone_number
    )
    return HttpResponse(f"Message sent to {phone_number}: {message.sid}")