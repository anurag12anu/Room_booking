from django.shortcuts import render,redirect,get_object_or_404
from  django.contrib.auth.hashers import check_password
from .forms import  Register_form,Login_form

from .Model.Auth_Model.auth import Auth_user

from django.http import HttpResponse



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
    
    else:  # Handle GET request
        form = Login_form()
        return render(request, 'hotel_app/login.html', {'form': form})
    
def user_logout(request):
    request.session.flush()
    return redirect('user_logi')

def home(request):
    if 'user_id' not in request.session:
        return redirect('user_logi')
    
    
    return render(request,'hotel_app/home.html')






