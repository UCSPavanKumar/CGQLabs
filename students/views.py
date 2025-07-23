from django.shortcuts import render
from twilio.rest import Client
from django.http import HttpResponse

def index(request):
    """
    landing page for the students app
    This page is the main entry point for the students app.
    It renders the index.html template.
    """
    return render(request, 'students/index.html')

def api_page(request):
    """
    API Information page for the students app
    """
    return render(request, 'students/api.html')

def automation_page(request):
    """
    Automation Information page for the students app
    """
    return render(request, 'students/automation.html')

def finance_page(request):
    """
    Finance Information page for the students app
    """
    return render(request, 'students/finance.html')

def contact_us(request):
    """
    Contact Us page for the students app
    This page allows users to contact the support team.
    """
    return render(request, 'students/contact_us.html')

def submit_contact_form(request):
    """
    Handle the contact form submission.
    This function processes the contact form data and sends an email.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save the data to a database
        # For demonstration, we will just return a success message
        return render(request, 'students/index.html', {'message': f'Thank you {name}, your message has been received!'})
        

    return HttpResponse('Invalid request method.', status=405)