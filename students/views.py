from django.shortcuts import render
from django.http import HttpResponse
from utils import sendmail    
from .models import contact
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

def cloud_page(request):
    """
    Cloud Services page for the students app
    This page provides information about cloud services offered.
    """
    return render(request, 'students/cloud.html')
def management(request):
    """
    Management page for the students app
    This page provides information about management services.
    """
    return render(request, 'students/management.html')

def submit_contact_form(request):
    """
    Handle the contact form submission.
    This function processes the contact form data and sends an email.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        #Validate form data
        if not name or not email or not message:
            return HttpResponse('All fields are required.', status=400)
        if '@' not in email or '.' not in email.split('@')[-1]:
            return HttpResponse('Invalid email address.', status=400)
        # Process the form data
        # Here we would typically save the data to a database or send an email
        # For demonstration, we will use a hypothetical sendmail utility
        # Assuming sendmail is a utility to send emails
        contact_entry = contact(name=name, email=email, message=message)
        contact_entry.save()  # Save the contact entry to the database
        # Send an email notification
        emailer = sendmail.SendMail(
            subject=f'Contact Form Submission from {name}',
            message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
            from_email='pavanupadrasta@gmail.com',
            recipient_list=['pomskipper09@gmail.com','support@techawake.in']
        )
        ret = emailer.send()
        print(ret)
        # Here you would typically send an email or save the data to a database
        # For demonstration, we will just return a success message
        return render(request, 'students/index.html', {'message': f'Thank you {name}, your message has been received!'})
        

    return HttpResponse('Invalid request method.', status=405)