from django.db import models
from hotel_app.Model.Hotel_Model.room_category import Room_Category



class Room(models.Model):
    room_number=models.CharField(max_length=10,unique=True)
    category=models.ForeignKey(Room_Category,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=True)
    
    def __str__(self):
        return f"Room{self.room_number} - {self.category.name}"
    
    