# gmail_sender_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', include('mailer.urls')),
]
