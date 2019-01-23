from __future__ import unicode_literals
from django.contrib import admin
from .models import JewelryType, Jewelry, Storage


class JewelryTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)


class JewelryAdmin(admin.ModelAdmin):
    list_display = ('jew_name', 'description', 'artist_name', 'price')


class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'type', 'price')

    def type(self, jew):
        return jew.jew_type.get_type_display()

    def name(self, name):
        return name.jewelry.jew_name

    def price(self, price):
        return price.jewelry.price


admin.site.register(JewelryType, JewelryTypeAdmin)
admin.site.register(Jewelry, JewelryAdmin)
admin.site.register(Storage, StorageAdmin)


