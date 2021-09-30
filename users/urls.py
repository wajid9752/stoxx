from django.contrib import admin
from django.urls import path,include
from .views import *

appname="users"
urlpatterns = [
    path('login/',              login,               name="login"     ),
    # path('login/',        dologin,            name="login"    ),
    path('register/',     register_view,      name="register" ),
    path('get_redirect/', get_redirect_if_exists,             ),
    # path('test/',         test,                  name="test"     ),
    path('logout/' ,      logout_view,           name="logout" ),
    # path('state_city/' ,  state_city,            name="state_city"  ),
    # path('inactive-user/',inactive_user  ,       name="inactive-user"),
    # path("profile-save/", complete_profile_save, name="profile-save"),
   
   
]