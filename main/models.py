from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255) 
    price = models.IntegerField()  
    description = models.TextField()  
    volume = models.IntegerField()

    
    @property
    def price_per_ml(self):
        return self.price / self.volume if self.volume > 0 else 0