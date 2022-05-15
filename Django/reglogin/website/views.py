from django.shortcuts import render
from website.models import user
from django.contrib import messages

# Create your views here.
def register_req(request):
    if request.method == "POST":
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
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def login_req(request):
    if request.method == 'POST':
        login_user = request.POST['y_name']
        login_passwd = request.POST['y_pass']
        try:
            user_obj = user.objects.get(username=login_user)
            if login_passwd == user_obj.password:
                request.session['logged_user'] = login_user
                return render(request, 'dashboard.html')
            else:
                messages.error(request, 'Incorrect password!')
        except:
            messages.error(request, 'User not found!')
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        del request.session['logged_user']
        return render(request,'login.html')
    return render(request,'dashboard.html')