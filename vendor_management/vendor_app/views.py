from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from vendor_app.models import Vendor, PurchaseOrder, HistoricalPerformance
from vendor_app.serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer


# Home view to serve a basic homepage template
def home_view(request):
    return render(request, 'home.html', {
        'welcome_message': 'Welcome to the Vendor Management System!'
    })


# Redirects to the Django admin interface
def redirect_to_admin(request):
    return HttpResponseRedirect(reverse('admin:index'))


# ViewSet for CRUD operations on Vendor
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]  # Require authentication for write operations


# ViewSet for CRUD operations on Purchase Order
class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Require authentication for write operations


# ViewSet to get Vendor performance metrics
class VendorPerformanceView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        # Fetch the vendor and ensure it exists
        try:
            vendor = Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=404)

        # Create a response with performance metrics
        performance_data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }

        return Response(performance_data, status=200)
