from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import tbl_admin
# Create your views here.

def user(request):
    if request.method == "POST":
        name = request.POST.get("txt_fname") + " " + request.POST.get("txt_lname")
        tbl_user.objects.create(user_name=name,
                                user_email=request.POST.get("txt_email"),
                                user_password=request.POST.get("txt_password"))
        return render(request,"Guest/User.html",{"msg":"Registred Sucessfully"})
    else:
        return render(request,"Guest/User.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=email,user_password=password)
            if user.user_status == 1:
                return render(request,"Guest/Login.html",{"msg":"Your Access is Denied By Administrator"})
            else:
                request.session["uid"] = user.id
                return redirect("User:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"] = admin.id
            return redirect("Admin:homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email or Password"})
    else:
        return render(request,"Guest/Login.html")

def index(request):
    return render(request,"Guest/index.html")