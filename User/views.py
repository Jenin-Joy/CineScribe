from django.shortcuts import render,redirect
from Admin.models import tbl_movie,tbl_crue
from User.models import *
from Guest.models import tbl_user
from django.http import JsonResponse
# Create your views here.

def homepage(request):
    if 'uid' in request.session:
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        movie = tbl_movie.objects.all()
        for i in movie:
            tot=0
            ratecount=tbl_rating.objects.filter(movie=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(movie=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    # print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(movie,parry)
        return render(request, 'User/Homepage.html',{'movie': datas,"ar":ar})
    else:
        return redirect('Guest:login')

def viewmovie(request):
    if 'uid' in request.session:
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        movie = tbl_movie.objects.all()
        for i in movie:
            tot=0
            ratecount=tbl_rating.objects.filter(movie=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(movie=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    # print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(movie,parry)
        return render(request, 'User/ViewMovie.html', {'movie': datas,"ar":ar})
    else:
        return redirect('Guest:login')

def viewcrue(request, id):
    crue = tbl_crue.objects.filter(movie=id)
    return render(request, 'User/ViewCrue.html', {"crue":crue})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(movie=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(movie=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,movie=tbl_movie.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(movie=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(movie=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(movie=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def searchmovie(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    movie = tbl_movie.objects.filter(movie_title__istartswith=request.GET.get("mname"))
    for i in movie:
        tot=0
        ratecount=tbl_rating.objects.filter(movie=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(movie=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                # print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(movie,parry)
    return render(request, "User/AjaxMovie.html",{'movie':datas,"ar":ar})

def profile(request):
    if 'uid' in request.session:
        user = tbl_user.objects.get(id=request.session["uid"])
        if request.method == "POST":
            user.user_name = request.POST.get("txt_name")
            user.user_email = request.POST.get("txt_email")
            user.save()
            return render(request, "User/Profile.html", {"msg":"Profile Updated"})
        else:
            return render(request, "User/Profile.html",{'user':user})
    else:
        return redirect('Guest:login')

def changepassword(request):
    if 'uid' in request.session:
        user = tbl_user.objects.get(id=request.session["uid"])
        if request.method == "POST":
            if request.POST.get("txt_opass") == user.user_password:
                if request.POST.get("txt_cpass") == request.POST.get("txt_npass"):
                    user.user_password = request.POST.get("txt_cpass")
                    user.save()
                    return render(request, "User/ChangePassword.html", {"msg1":"Password Changed"})
                else:
                    return render(request, "User/ChangePassword.html", {"msg":"New Password and Confirm Password does not match"})
            else:
                return render(request, "User/ChangePassword.html", {"msg":"Old Password Incorrect"})
        else:
            return render(request, "User/ChangePassword.html")
    else:
        return redirect('Guest:login')

def logout(request):
    del request.session["uid"]
    return redirect("Guest:login")