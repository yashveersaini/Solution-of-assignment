from django.core.management.base import BaseCommand
from django.db import transaction
import threading

from signals_app.signals import demo_signal
from signals_app.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        print("\nQUESTION 1")
        print("Before Signal")

        demo_signal.send(sender=self.__class__)

        print("After Signal")

        print("\nQUESTION 2")
        print("Caller Thread ID:", threading.get_ident())

        demo_signal.send(sender=self.__class__)

        print("\nQUESTION 3")

        try:
            with transaction.atomic():

                Product.objects.create(
                    name="Test Product"
                )

                raise Exception("Rollback")

        except Exception:
            print("Transaction Rolled Back")

        count = Product.objects.filter(
            name="Test Product"
        ).count()

        print("Rows in Database:", count)