from django.urls import path
from home import views

urlpatterns = [
    # Homepage
    path('', views.index, name='home'),

    # Auth
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    
    # Custom styling (if needed for static/style views)
    #path('style/', views.style, name='style'),
    path('registerstyle/', views.registerstyle, name='registerstyle'),

    # Post-login screen
    path('loginmain/', views.loginmain, name='mainscreen'),

    # Job details & application
    path('microabout/', views.microabout, name='microabout'),
    path('microapply/', views.microapply, name='microapply'),

    path('amazonabout/', views.amazonabout, name='amazonabout'),
    path('amazonapply/', views.amazonapply, name='amazonapply'),

    path('mahindratechabout/', views.mahindratechabout, name='mahindratechabout'),
    path('mahindratechapply/', views.mahindratechapply, name='mahindratechapply'),
    path('techmahindraapply/', views.techmahindraapply, name='techmahindraapply'),

    # Job categories
    path('remote/', views.remote, name='remote'),
    path('sales/', views.sales, name='sales'),
    path('mnc/', views.mnc, name='mnc'),
    path('softit/', views.softit, name='softit'),
    path('engineering/', views.eng, name='eng'),
    path('marketing/', views.marketing, name='marketing'),

    # Static pages
    path('aboutus/', views.about, name='about'),
]
