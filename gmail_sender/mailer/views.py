# gmail_sender/views.py

from django.shortcuts import render, redirect
from .form import EmailForm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Get email details from the form
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Your Gmail credentials and app password
            gmail_user = 'albin99.in@gmail.com'
            gmail_password = 'ersn cdzm uzbz tdhi'


            # Set up the message
            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Connect to Gmail SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(gmail_user, gmail_password)
                server.sendmail(gmail_user, to_email, msg.as_string())

            return redirect('success')  # Redirect to the success page

    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})

def success(request):
    return render(request, 'success.html')
