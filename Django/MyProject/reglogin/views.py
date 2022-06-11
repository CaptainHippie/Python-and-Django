from django.shortcuts import render
from django.contrib import messages
from . models import user

def login_req(request):
    if 'signinbtn' in request.POST:
        login_user = request.POST['y_name']
        login_passwd = request.POST['y_pass']
        try:
            user_obj = user.objects.get(username=login_user)
            if login_passwd == user_obj.password:
                request.session['logged_user'] = login_user 
                print("SUCCESS",user_obj.username)               
                return render(request, 'dash_new.html', {"userinfo": user_obj})
            else:
                messages.error(request, 'Incorrect password!')
                return render(request, 'loginreg.html')
        except:
            messages.error(request, 'User not found!')
            return render(request, 'loginreg.html')
    elif 'signupbtn' in request.POST:
        nm = request.POST['namebox']
        em = request.POST['emailbox']
        un = request.POST['unamebox']
        pas = request.POST['passbox']
        cpas = request.POST['re_passbox']
        if pas == cpas:
            user(name=nm,email=em,username=un,password=pas).save(force_insert='__all__')
            messages.success(request, 'New user ' + un + ' is successfully registered')
        else:
            messages.error(request, 'password does not match!')
        return render(request, 'loginreg.html')
    else:
        return render(request, 'loginreg.html')

def logout(request):
    if request.method == 'POST':
        del request.session['logged_user']
        return render(request,'loginreg.html')
    return render(request,'dash_new.html')

