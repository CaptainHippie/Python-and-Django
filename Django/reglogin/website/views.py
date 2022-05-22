from django.shortcuts import render
from website.models import user
from django.contrib import messages

# Create your views here.

def login_req(request):
    if 'signinbtn' in request.POST:
        login_user = request.POST['y_name']
        login_passwd = request.POST['y_pass']
        try:
            user_obj = user.objects.get(username=login_user)
            if login_passwd == user_obj.password:
                request.session['logged_user'] = login_user                
                return render(request, 'dash_new.html', {"userdata": user_obj})
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

def edit(request):
    login_user = request.session['logged_user']
    user_obj = user.objects.get(username=login_user)
    return render(request,'edit_user.html', {"userdata": user_obj})

def update(request):
    login_user = request.session['logged_user']
    user_obj = user.objects.get(username=login_user)
    if request.method == 'POST':
        nm = request.POST['namebox']
        em = request.POST['emailbox']
        un = request.POST['unamebox']
        user(name=nm,email=em,username=un).save()
        cpas = request.POST['cur_passbox']
        npas = request.POST['new_passbox']
        cfpas = request.POST['re_passbox']
        if request.POST['cur_passbox']:
            print("BUAAAAA")
        messages.success(request,"The Student Record is updated succesfully....")
        return render(request, 'edit_user.html')
    else:
        return render(request, 'edit_user.html')





#################     Insertion  ##################
'''

########## Edit ##############
def stedit(request, sid):
    edit = user()
    getstudata = user.objects.get(sid=sid)
    return render(request, 'edit.html', {"Stud": getstudata})


##############################
def stupdate(request, sid):
    stupdate = user.objects.get(sid=sid)
    form = stform(request.POST, instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The Student Record is updated succesfully....")
        return render(request, 'edit.html', {"Stud": stupdate})
    else:
        return render(request, 'edit.html')'''

