from django.db import models
from categories.models import Brand

class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/media/uploads/', blank=True, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title