###
### Don't Pay The State!
### Author: Kenneth Miller
###
### Thise file defines "handlers" or actions that are trigged on certain events.
###

### IMPORTS
from django.db.models.signals import post_save, post_delete
from dontpaythestate.remember.models import *
from django.core.mail import send_mail

import uuid

#define the web_url
web_url = "http://www.dontpaythestate.com"


def subscribe_handler(sender, instance, created, **kwargs):
    """This handler is fired when a Subscription object is created."""
    #if created:
    #    t = InactiveUsers(email_address=instance.email_address,uid=uuid.uuid4().hex)
    #    t.save()

    send_mail('Thanks for Registering!', 
              'Use the URL below to confirm.\r %s' % (web_url + '/activate/' + t.uid),
              'noreply@dontpaythestate.com',
              [instance.email_address], fail_silently=False)

post_save.connect(subscribe_handler, sender=Subscription)

def confirm_handler(sender, instance, **kwargs):
    send_mail("You're Registered!", 
              'Thanks for registering!',
              'noreply@dontpaythestate.com',
              [instance.email_address], fail_silently=False)

#post_delete.connect(confirm_handler, sender=InactiveUsers)
