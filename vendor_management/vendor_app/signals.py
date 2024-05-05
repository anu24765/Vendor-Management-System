from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, created, **kwargs):
    vendor = instance.vendor

    # Update metrics when a purchase order is completed
    if instance.status == 'completed':
        # On-Time Delivery Rate
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        on_time_pos = completed_pos.filter(delivery_date__lte=instance.delivery_date)
        total_pos = completed_pos.count()
        if total_pos:
            vendor.on_time_delivery_rate = (on_time_pos.count() / total_pos) * 100

        # Quality Rating Average
        quality_ratings = completed_pos.filter(quality_rating__isnull=False).values_list("quality_rating", flat=True)
        if quality_ratings:
            vendor.quality_rating_avg = sum(quality_ratings) / len(quality_ratings)

        # Fulfillment Rate
        successful_fulfillments = completed_pos.count()
        if total_pos:
            vendor.fulfillment_rate = (successful_fulfillments / total_pos) * 100

    # Update average response time when an order is acknowledged
    if instance.acknowledgment_date:
        response_times = [
            po.acknowledgment_date - po.issue_date for po in PurchaseOrder.objects.filter(
                vendor=vendor, acknowledgment_date__isnull=False
            )
        ]
        if response_times:
            vendor.average_response_time = sum(
                rt.total_seconds() for rt in response_times
            ) / len(response_times)

    vendor.save()


@receiver(post_delete, sender=PurchaseOrder)
def recalculate_vendor_metrics(sender, instance, **kwargs):
    # Trigger metric recalculations on deletion of a purchase order
    update_vendor_performance(sender, instance, created=False, **kwargs)
