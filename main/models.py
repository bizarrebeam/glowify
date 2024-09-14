import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) 
    price = models.IntegerField()  
    description = models.TextField()  
    volume = models.IntegerField()

    @property
    def price_per_ml(self):
        return self.price / self.volume if self.volume > 0 else 0