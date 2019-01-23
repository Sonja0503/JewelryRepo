from rest_framework import serializers
from .models import JewelryType, Jewelry, Storage


class JewelryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JewelryType
        fields = (
            'type',
        )


class JewelrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = (
            'jew_name',
            'description',
            'artist_name',
            'price'
        )


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = (
            'quantity',
            'jewelry',
            'jew_type',
        )
