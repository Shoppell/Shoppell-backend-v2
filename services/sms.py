from random import randint
from .models import User
from django.utils.timezone import timedelta
from django.utils import timezone
from melipayamak import Api

username = '09930731973'
password = 'D9HTC'

def send_custom_text(phone, text): 
    api = Api(username, password)
    sms_rest = api.sms()
    text = [text, ]
    to = phone
    bodyId = 81020
    return sms_rest.send_by_base_number(text, to, bodyId)

