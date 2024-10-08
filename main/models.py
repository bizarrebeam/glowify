import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) 
    price = models.IntegerField()  
    description = models.TextField()  
    volume = models.IntegerField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)

    @property
    def price_per_ml(self):
        return self.price / self.volume if self.volume > 0 else 0
