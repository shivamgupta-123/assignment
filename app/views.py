from django.shortcuts import render, redirect, HttpResponse
from .models import Signup
import uuid
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        email = request.POST.get('email')
        image = request.FILES['image']
        id = uuid.uuid4().hex[:6].upper()
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        result = Signup.objects.filter(email=email).exists()
        print(result)
        if result == False:
            if len(password)>=8:
                if password == confirm_password:
                    data = Signup(first_name=first_name, last_name=last_name, Age=age, id=id, email=email, password=password,
                              confirm_password=confirm_password, image=image)
                    data.save()
                    messages.success(request, "Your Account Successful Created!")
                    return redirect('/')
                else:
                    messages.error(request, "Your Password and Confirm Password is not same!")
                    return redirect('/')
            else:
                messages.error(request, "Password should be minimum 8 Characters!")
                return redirect('/')
        messages.success(request, "This Email ID already Exists!")
        return redirect('/')
    return render(request, 'home.html')


def login(request):
    if request.session.has_key('data'):
        detai = request.session.get('data')
        detail = Signup.objects.get(email=detai)
        return render(request, 'detail.html', {'detail': detail})
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            result = Signup.objects.get(email=email)
            psw = result.password
            request.session['data'] = email
        except Signup.DoesNotExist:
            messages.error(request, "This Email ID doesn't Exist!")
            return redirect('/login')
        if password == psw:
            detail = Signup.objects.get(email=email)
            return render(request, 'detail.html', {'detail': detail})
        else:
            messages.error(request, "Your Password isn't Correct! ")
            return redirect('/login')
    return render(request, 'login.html')

def logout(request):
    if request.session.has_key('data'):
        del request.session['data']
        return redirect('/login')
    return redirect('/login')