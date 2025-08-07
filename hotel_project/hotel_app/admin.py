from django.contrib import admin


from hotel_app.Model.Hotel_Model.customer import Customer
from hotel_app.Model.Hotel_Model.room import Room
from hotel_app.Model.Hotel_Model.room_category import Room_Category
from hotel_app.Model.Hotel_Model.booking import Room_Booking

admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Room_Category)
admin.site.register(Room_Booking)