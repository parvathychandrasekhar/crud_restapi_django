from django.db import models


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name