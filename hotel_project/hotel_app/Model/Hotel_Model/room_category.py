from django.db import models

class Room_Category(models.Model):
    name=models.CharField(max_length=50)
    prise=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    