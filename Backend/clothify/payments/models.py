from django.db import models
import uuid
from orders.models import Order

# Create your models here.
class Payment(models.Model):
    PROVIDER_CHOICES = (
        ('M-pesa', 'M-PESA'),
        ('Stripe', 'Stripe'),
    )
    STATUS_CHOICES = (
        ('Initiated', 'INITIATED'),
        ('Success', 'SUCCESS'),
        ('Failed', 'FAILED'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField(Order, related_name="payment", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    checkout_request_id = models.CharField(max_length=255, unique=True)
    merchant_request_id = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Initiated')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MPESA {self.status} | Order {self.order.id}"