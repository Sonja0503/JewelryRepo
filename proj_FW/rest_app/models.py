from __future__ import unicode_literals
from django.db import models


class JewelryType(models.Model):
    TYPE = (
        (1, 'Necklace'),
        (2, 'Ring'),
        (3, 'Piercing'),
        (4, 'Other'),
    )

    type = models.PositiveSmallIntegerField(choices=TYPE)

    def __str__(self):
        return '{}'.format(self.get_type_display())


class Jewelry(models.Model):
    jew_name = models.CharField(max_length=10)
    description = models.TextField(max_length=100)
    artist_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return '{}, {}'.format(self.jew_name, self.artist_name)


class Storage(models.Model):
    quantity = models.IntegerField(default=0)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    jew_type = models.ForeignKey(JewelryType, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.quantity, self.jewelry.jew_name, self.jew_type.get_type_display())
