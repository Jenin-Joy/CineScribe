from django.urls import path
from Admin import views
app_name = "Admin"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path("genre/",views.genre,name="genre"),
    path("deletegenre/<int:id>",views.deletegenre,name="deletegenre"),
    path("editgenre/<int:id>",views.editgenre,name="editgenre"),

    path("cruetype/",views.cruetype,name="cruetype"),
    path("deletecruetype/<int:id>",views.deletecruetype,name="deletecruetype"),
    path("editcruetype/<int:id>",views.editcruetype,name="editcruetype"),

    path("admin/",views.admin,name="admin"),
    path("deleteadmin/<int:id>",views.deleteadmin,name="deleteadmin"),

    path("movie/",views.movie,name="movie"),
    path("deletemovie/<int:id>",views.deletemovie,name="deletemovie"),

    path("crue/<int:id>",views.crue,name="crue"),
    path("deletecrue/<int:id>",views.deletecrue,name="deletecrue"),

    path("user/",views.user,name="user"),
    path("verifyuser/<int:id>/<int:status>",views.verifyuser,name="verifyuser"),
    path("rejecteduser/",views.rejecteduser,name="rejecteduser"),

    path('logout/',views.logout,name="logout"),


]