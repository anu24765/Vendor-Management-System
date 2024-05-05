Here's a shorter version of the API documentation, focusing on key details and examples:

---

# Vendor Management System API

The Vendor Management System API provides endpoints for managing vendors, purchase orders, and evaluating vendor performance. Here's a quick guide to the available endpoints.

## Base URL
All endpoints use this base URL:
```
http://127.0.0.1:8000/api/
```

## Vendor Management

### Create a New Vendor
- **Method**: POST
- **Endpoint**: `/vendors/`
- **Body**:
  ```json
  {
    "name": "Vendor Name",
    "contact_details": "1234567890",
    "address": "Vendor Address",
    "vendor_code": "1"
  }
  ```
- **Response**: 201 Created with the new vendor's details.

### List All Vendors
- **Method**: GET
- **Endpoint**: `/vendors/`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Vendor 1",
      "contact_details": "1234567890"
    }
  ]
  ```

### Get Vendor Details
- **Method**: GET
- **Endpoint**: `/vendors/{vendor_id}/`
- **Response**: 200 OK with the vendor's details.

### Update a Vendor
- **Method**: PUT
- **Endpoint**: `/vendors/{vendor_id}/`
- **Body**:
  ```json
  {
    "name": "Updated Name",
    "contact_details": "9876543210"
  }
  ```

### Delete a Vendor
- **Method**: DELETE
- **Endpoint**: `/vendors/{vendor_id}/`
- **Response**: 204 No Content on success.

## Purchase Order Tracking

### Create a Purchase Order
- **Method**: POST
- **Endpoint**: `/purchase_orders/`
- **Body**:
  ```json
  {
    "po_number": "1",
    "order_date": "2024-05-01T14:02:00Z",
    "delivery_date": "2024-05-02T14:02:00Z",
    "items": {
      "phone": "iPhone 13"
    },
    "quantity": 1,
    "status": "pending"
  }
  ```

### List All Purchase Orders
- **Method**: GET
- **Endpoint**: `/purchase_orders/`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "po_number": "1",
      "order_date": "2024-05-01T14:02:00Z"
    }
  ]
  ```

### Get Purchase Order Details
- **Method**: GET
- **Endpoint**: `/purchase_orders/{po_id}/`
- **Response**: 200 OK with the order's details.

### Update a Purchase Order
- **Method**: PUT
- **Endpoint**: `/purchase_orders/{po_id}/`
- **Body**:
  ```json
  {
    "status": "delivered"
  }
  ```

### Delete a Purchase Order
- **Method**: DELETE
- **Endpoint**: `/purchase_orders/{po_id}/`
- **Response**: 204 No Content on success.

## Vendor Performance Evaluation

### Get Vendor Performance
- **Method**: GET
- **Endpoint**: `/vendors/{vendor_id}/performance`
- **Response**:
  ```json
  {
    "on_time_delivery_rate": 95.0,
    "quality_rating_avg": 4.0,
    "average_response_time": 30.0
  }
  ```

---
