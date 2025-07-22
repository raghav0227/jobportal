from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("login.html",views.login,name='login'),
    path('',views.style),
    path("register.html",views.register,name='register'),
     path("register",views.register,name='register'),
   path('',views.registerstyle),
    path("loginmain.html",views.loginmain,name='mainscreen'),
    path("microabout.html",views.microabout,name='microabout'),
    path("microapply.html",views.microapply,name='microapply'),
    path("microapply",views.microapply,name='microapply'),
    path("amazonabout.html",views.amazonabout,name='amazonabout'),
    path("amazonapply.html",views.amazonapply,name='amazonapply'),
    path("amazonapply",views.amazonapply,name='amazonapply'),
    path("mahindratechabout.html",views.mahindratechabout,name='mahindratechabout'),
    path("mahindratechapply.html",views.mahindratechapply,name='mahindratechapply'),
    path("techmahindraapply",views.techmahindraapply,name='techmahindraapply'),
    path("remote.html",views.remote,name='remote'),
    path("sales.html",views.sales,name='sales'),
    path("mnc.html",views.mnc,name='mnc'),
    path("softit.html",views.softit,name='softit'),
    path("engineering.html",views.eng,name='eng'),
    path("marketing.html",views.marketing,name='marketing'),
    path("aboutus.html",views.about,name='about'),
    ]
