from django.shortcuts import render,redirect,get_object_or_404
from  django.contrib.auth.hashers import check_password
from .forms import  Register_form,Login_form,Booking_Form




from .Model.Auth_Model.auth import Auth_user

from django.http import HttpResponse

from hotel_app.Model.Hotel_Model.booking import Room_Booking
from hotel_app.Model.Hotel_Model.room import Room



def user_register(request):
    if request.method =='POST':
        form=Register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_logi')
    else:
        form =Register_form()
    return render(request,'hotel_app/register.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        login_form=Login_form(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            try:
                user=Auth_user.objects.get(username=username)
                if check_password(password,user.password):
                    request.session['user_id']=user.id
                    request.session['user_name']=user.username
                    return redirect('home_page')
                else:
                   return HttpResponse('Invalid username or password')
                    
            except Auth_user.DoesNotExist:
                
                return HttpResponse('user data not found')
        else:
            form = Login_form()    
        

        return render(request, 'hotel_app/login.html',{'form':form})
    
    else:  
        form = Login_form()
        return render(request, 'hotel_app/login.html', {'form': form})
    
def user_logout(request):
    request.session.flush()
    return redirect('user_logi')

def home(request):
    if 'user_id' not in request.session:
        return redirect('user_logi')
    
    
    return render(request,'hotel_app/home.html')

def room_list(request):
    rooms =Room.objects.all()
    return render(request,'hotel_app/room_list.html',{'rooms':rooms})
    pass
def book_room(request,room_id):
    room=get_object_or_404(Room,id=room_id)
    if request.method == 'POST':
        form=Booking_Form(request.POST)
        if form.is_valid():
            customer =form.save()
            Room_Booking.objects.create(
                customer=customer,
                room=room,
                check_in=form.cleaned_data['check_in'],
                check_out=form.cleaned_data['check_out']
            )
            room.is_available=False
            room.save()
            return redirect('history_booking')
    else:
        booking_forms=Booking_Form()
    return render(request,'hotel_app/room_booking.html',{'form':booking_forms,'rooms':room})
        
def booking_history(request):
    bookings=Room_Booking.objects.all().order_by('-booked_on')
    return render(request,'hotel_app/booking_history.html',{'booking_history':bookings})
    





