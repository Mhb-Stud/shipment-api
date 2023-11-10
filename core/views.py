from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from core.models import Article, Shipment
from rest_framework import serializers

class ShipmentListAPIView(APIView):

    class ShipmentSerializer(serializers.ModelSerializer):
        class ArticleSerializer(serializers.ModelSerializer):
            class Meta:
                model = Article
                fields = '__all__'

        articles = ArticleSerializer(many=True, read_only=True)

        class Meta:
            model = Shipment
            fields = '__all__'

    # add prefetch_related
    def get(self, request):
        shipments = Shipment.objects.prefetch_related('articles').all()
        paginator = PageNumberPagination()
        paginated_shipments = paginator.paginate_queryset(shipments, request=request)
        serializer = self.ShipmentSerializer(paginated_shipments, many=True)
        return paginator.get_paginated_response(serializer.data)



class ShipmentByTrackingNumberView(APIView):
    class ShipmentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Shipment
            fields = '__all__'

    def get(self, request, tracking_number):
        shipments = Shipment.objects.filter(tracking_number=tracking_number)
        paginator = PageNumberPagination()
        paginated_shipments = paginator.paginate_queryset(shipments, request=request)
        serializer = self.ShipmentSerializer(paginated_shipments, many=True)
        return paginator.get_paginated_response(serializer.data)

class ShipmentByCarrierView(APIView, PageNumberPagination):
    class ShipmentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Shipment
            fields = '__all__'

    def get(self, request, carrier):
        shipments = Shipment.objects.filter(carrier=carrier)
        paginator = PageNumberPagination()
        paginated_shipments = paginator.paginate_queryset(shipments, request=request)
        serializer = self.ShipmentSerializer(paginated_shipments, many=True)
        return paginator.get_paginated_response(serializer.data)