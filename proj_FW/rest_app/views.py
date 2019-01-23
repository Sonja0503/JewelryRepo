from __future__ import unicode_literals
from .models import JewelryType, Jewelry, Storage
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import JewelryTypeSerializer, JewelrySerializer, StorageSerializer


class JewelryTypeList(ListAPIView):
    serializer_class = JewelryTypeSerializer

    def get_queryset(self):
        qs = JewelryType.objects.all()
        jt = self.request.query_params.get('type')
        if jt:
            qs = qs.filter(type=jt)
        return qs


class JewelryList(ListAPIView):
    serializer_class = JewelrySerializer

    def get_queryset(self):
        qs = Jewelry.objects.all()
        jn = self.request.query_params.get('name')
        if jn:
            qs = qs.filter(jew_name__icontains=jn)
        return qs


class StorageList(ListAPIView):
    serializer_class = StorageSerializer

    def get_queryset(self):
        qs = Storage.objects.all()
        an = self.request.query_params.get('name')
        if an:
            qs = qs.filter(jewelry__artist_name=an)
        return qs

