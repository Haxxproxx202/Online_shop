from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Send an email after a successful form submission.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order no {order.id}"
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@email.com',
                          [order.email])
    print("Tu działa")
    print(order.email)
    return mail_sent
