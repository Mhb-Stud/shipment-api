from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import *

urlpatterns = [
    path('shipments/tracking/<str:tracking_number>/', ShipmentByTrackingNumberView.as_view(), name='shipment-by-tracking'),
    path('shipments/carrier/<str:carrier>/', ShipmentByCarrierView.as_view(), name='shipment-by-carrier'),
    path('shipments/', ShipmentListAPIView.as_view(), name='shipment-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)