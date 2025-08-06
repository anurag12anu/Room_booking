from django.db import models
from hotel_app.Model.Hotel_Model.customer import Customer
from hotel_app.Model.Hotel_Model.room import Room

class Room_Booking(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    booked_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.name} - {self.room.room_number}"