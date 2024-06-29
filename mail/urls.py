from django.urls import path
from .views import sendmail, send_notify2

urlpatterns = [
    path('send/<keys>/<email>/', sendmail),
    path('send_to/<sender>/<password>/<email_to>/<keys>/', send_notify2),
]
