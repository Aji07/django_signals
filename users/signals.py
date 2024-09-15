import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal to check if it's running synchronously
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    # Check if the signal runs synchronously by adding a sleep
    print("Signal received: Starting long task...")
    time.sleep(3)
    print("Signal task finished.")
    
    # Check if it's running in the same thread
    print(f"Signal thread: {threading.current_thread().name}")
    
    # Check if the signal runs inside a transaction
    if transaction.get_connection().in_atomic_block:
        print("Signal executed inside a transaction")
    else:
        print("Signal executed outside of a transaction")
