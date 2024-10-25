from django.urls import path
from User import views
app_name = "User"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path("viewmovie/",views.viewmovie,name="viewmovie"),
    path("viewcrue/<int:id>",views.viewcrue,name="viewcrue"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('searchmovie/',views.searchmovie,name="searchmovie"),
    path('profile/',views.profile,name="profile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('logout/',views.logout,name="logout"),


]