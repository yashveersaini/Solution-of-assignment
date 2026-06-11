from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from .models import Product

import threading
import time

demo_signal = Signal()


@receiver(demo_signal)
def demo_receiver(sender, **kwargs):
    print("Receiver Started")
    print("Receiver Thread ID:", threading.get_ident())

    time.sleep(5)

    print("Receiver Finished")


@receiver(post_save, sender=Product)
def product_receiver(sender, instance, **kwargs):
    print("Signal Executed")