from django.db import models
from django.utils import timezone  # For timestamps
from django.db.models import JSONField  # JSON support for Django >= 4.1


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField()
    items = JSONField()  # Contains details of the items in the purchase order
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')  # E.g., 'pending', 'completed', 'canceled'
    quality_rating = models.FloatField(null=True, blank=True)  # Rating of quality (nullable)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)  # Record creation time
    on_time_delivery_rate = models.FloatField(default=0.0)  # Historical on-time rate
    quality_rating_avg = models.FloatField(default=0.0)  # Historical quality rating
    average_response_time = models.FloatField(default=0.0)  # Historical response time in seconds
    fulfillment_rate = models.FloatField(default=0.0)  # Historical fulfillment rate

    def __str__(self):
        return f"Performance record for {self.vendor.name} on {self.date}"

