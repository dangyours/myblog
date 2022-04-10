from django.urls import path
from . import views 

urlpatterns = [
    path('login',views.login,name = "user_login"),
    path('dologin',views.dologin,name = "user_dologin"),
    path('logout',views.logout,name = "user_logout"),
    path('register',views.register,name = "user_register"),
    path('doregister',views.doregister,name = "user_doregister"),
]