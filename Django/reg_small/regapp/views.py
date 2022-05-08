from django.shortcuts import render
from django.contrib import messages
from regapp.models import userreg

# Create your views here.
def UserRegistration(request):
    if request.method=="POST":
        if request.POST.get("namebox") and request.POST.get("emailbox") and request.POST.get("unamebox") and request.POST.get("passwdbox"):
            saverecord = userreg()
            saverecord.name = request.POST.get("namebox")
            saverecord.email = request.POST.get("emailbox")
            saverecord.uname = request.POST.get("unamebox")
            saverecord.passwd = request.POST.get("passwdbox")
            saverecord.save()
            messages.success(request,"New user registration details saved successfully!")
            return render(request,"index.html")
    else:
        return render(request,"index.html")