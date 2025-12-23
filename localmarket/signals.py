from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    messages.success(request, "Konto zostało utworzone pomyślnie!")
