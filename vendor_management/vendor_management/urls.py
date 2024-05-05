from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendor_app import views  # Importing views from your Django app

# Create a DefaultRouter instance to generate RESTful API endpoints
router = DefaultRouter()

# Register viewsets with the router
router.register(r'vendors', views.VendorViewSet)  # CRUD operations for vendors
router.register(r'purchase_orders', views.PurchaseOrderViewSet)  # CRUD operations for purchase orders

# Define the URL patterns for the project
urlpatterns = [
    path('', views.home_view),  # Route for the root URL (home page)
    path('admin/', admin.site.urls),  # Django admin interface
    path('api/', include(router.urls)),  # Include RESTful endpoints managed by the router
    path('api/vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view({'get': 'retrieve'})),  # Endpoint for vendor performance metrics
]
