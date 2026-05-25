
from django.contrib import admin
from django.urls import path, include
from movie_downloader  import views
from django. conf import settings
from django. conf.urls.static import static
urlpatterns = [
    path("",views.index, name='movie_downloader'),
    path("login.html",views.login, name='logon'),
    path("about",views.about, name='about'),
    path("signup.html",views.signup, name='signup'),
    path("register",views.register,name='register'),
    path("login",views.loginn,name='login'),
    path("home",views.home,name='home'),
    path("movies",views.movie,name="movie"),
    path("add",views.add,name="addmovie"),
    path("logout",views.logoutt,name="logout"),
    path('player/<str:tlink>/<str:name>/<str:description>', views.player, name='player'),
    path("contact",views.contact,name="contact"),
    path("sendemail",views.send_email,name="sendemail"),
    path("mplayer/<str:mlink>/<str:name>/<str:description>", views.video_player, name='mplayer')
    











]
 