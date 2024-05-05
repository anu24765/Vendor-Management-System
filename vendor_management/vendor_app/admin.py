from django.contrib import admin

from .models import Vendor, PurchaseOrder, HistoricalPerformance # Import your models

# Register the models with the Django admin
admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)
