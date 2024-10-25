from django.shortcuts import render,redirect
from Admin.models import *
from User.models import tbl_rating
from Guest.models import tbl_user
# Create your views here.

def homepage(request):
    if 'aid' in request.session:
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
        return render(request,"Admin/Homepage.html",{"movie":datas})
    else:
        return redirect("Guest:login")

def genre(request):
    if 'aid' in request.session:
        gen = tbl_genre.objects.all()
        if request.method == "POST":
            tbl_genre.objects.create(genre_name=request.POST.get('txt_genre'))
            return render(request,"Admin/Genre.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Genre.html",{"genre":gen})
    else:
        return redirect("Guest:login")

def deletegenre(request, id):
    tbl_genre.objects.get(id=id).delete()
    return render(request,"Admin/Genre.html",{"msg":"Data Deleted"})

def editgenre(request, id):
    gen = tbl_genre.objects.get(id=id)
    if request.method == "POST":
        gen.genre_name = request.POST.get('txt_genre')
        gen.save()
        return render(request,"Admin/Genre.html",{"msg":"Data Updated"})
    else:
        return render(request,"Admin/Genre.html",{"genreedit":gen})

def cruetype(request):
    if 'aid' in request.session:
        types = tbl_cruetype.objects.all()
        if request.method == "POST":
            tbl_cruetype.objects.create(cruetype_name=request.POST.get('txt_type'))
            return render(request,"Admin/Type.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Type.html",{"type":types})
    else:
        return redirect("Guest:login")

def deletecruetype(request, id):
    tbl_cruetype.objects.get(id=id).delete()
    return render(request,"Admin/Type.html",{"msg":"Data Deleted"})

def editcruetype(request, id):
    types = tbl_cruetype.objects.get(id=id)
    if request.method == "POST":
        types.cruetype_name = request.POST.get('txt_type')
        types.save()
        return render(request,"Admin/Type.html",{"msg":"Data Updated"})
    else:
        return render(request,"Admin/Type.html",{"typeedit":types})

def admin(request):
    if 'aid' in request.session:
        admin = tbl_admin.objects.all()
        if request.method == "POST":
            tbl_admin.objects.create(admin_name=request.POST.get('txt_name'),admin_email=request.POST.get('txt_email'),admin_contact=request.POST.get('txt_contact'),admin_password=request.POST.get('txt_password'))
            return render(request,"Admin/Admin.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/Admin.html",{"admin":admin})
    else:
        return redirect("Guest:login")

def deleteadmin(request, id):
    tbl_admin.objects.get(id=id).delete()
    return render(request,"Admin/Admin.html",{"msg":"Data Deleted"})

def movie(request):
    if 'aid' in request.session:
        genre = tbl_genre.objects.all()
        movie = tbl_movie.objects.all()
        if request.method == "POST":
            tbl_movie.objects.create(movie_title=request.POST.get("txt_title"),
                                    movie_release_date=request.POST.get("txt_date"),
                                    movie_description=request.POST.get("txt_description"),
                                    movie_poster=request.FILES.get("txt_poster"),
                                    movie_link=request.POST.get("txt_link"),
                                    genre=tbl_genre.objects.get(id=request.POST.get("sel_genre")))
            return render(request,"Admin/AddMovie.html",{"msg":"Data Inserted"})
        else:
            return render(request,"Admin/AddMovie.html",{"movie":movie,"genre":genre})
    else:
        return redirect("Guest:login")

def deletemovie(request, id):
    tbl_movie.objects.get(id=id).delete()
    return render(request,"Admin/AddMovie.html",{"msg":"Data Deleted"})

def crue(request, id):
    types = tbl_cruetype.objects.all()
    crue = tbl_crue.objects.all()
    if request.method == "POST":
        tbl_crue.objects.create(crue_name=request.POST.get('txt_name'),crue_photo=request.FILES.get('txt_photo'),cruetype=tbl_cruetype.objects.get(id=request.POST.get("sel_type")),movie=tbl_movie.objects.get(id=id))
        return render(request,"Admin/AddCrue.html",{"msg":"Data Inserted","id":id})
    else:
        return render(request,"Admin/AddCrue.html",{"crue":crue,"cruetype":types})

def deletecrue(request, id):
    tbl_crue.objects.get(id=id).delete()
    return render(request,"Admin/AddCrue.html",{"msg":"Data Deleted"})

def user(request):
    if 'aid' in request.session:
        user = tbl_user.objects.filter(user_status=0)
        return render(request,"Admin/User.html",{"user":user})
    else:
        return redirect("Guest:login")

def verifyuser(request, id, status):
    user = tbl_user.objects.get(id=id)
    user.user_status = status
    user.save()
    return render(request,"Admin/Homepage.html",{"msg":"User Verified","status":status})

def rejecteduser(request):
    if 'aid' in request.session:
        user = tbl_user.objects.filter(user_status=1)
        return render(request,"Admin/RejectedUser.html",{"user":user})
    else:
        return redirect("Guest:login")

def logout(request):
    del request.session["aid"]
    return redirect("Guest:login")