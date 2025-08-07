from django.urls import path
from . import views


urlpatterns=[
    path('user_register/',views.user_register,name='user_regi'),
    path('user_login/',views.user_login,name='user_logi'),
    path('user_logout/',views.user_logout,name='user_logo'),
    
    path('',views.home,name='home_page'),
    path('book_room/<int:room_id>/',views.book_room, name='room_book'),
    path('room_list/',views.room_list, name='list_room'),
    path('book_history/',views.booking_history, name='history_booking'),
    
    
]