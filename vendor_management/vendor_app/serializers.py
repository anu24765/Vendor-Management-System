from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'  # Serialize all fields of the Vendor model


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        # If 'items' is required, ensure it has 'required=True'
        extra_kwargs = {
            'items': {'required': True},  # Explicitly mark as required
        }


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'  # Serialize all fields of the HistoricalPerformance model
