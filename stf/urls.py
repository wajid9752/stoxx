from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',              home,               name="home"),
    path('blog/',     blog,                   name="blog" ),
    path('contact/',        contact,          name="contact"),
    path('carrer/',     carrer,               name="carrer"),
    path('job/<int:pk>/', job_view,           name="job_view"),
    path('resume/',         resume,                  name="resume"     ),
    # path('logout/' ,      logout_view,           name="logout" ),
    # path('state_city/' ,  state_city,            name="state_city"  ),
    # path('inactive-user/',inactive_user  ,       name="inactive-user"),
    # path("profile-save/", complete_profile_save, name="profile-save"),
    # path('category/',     category,              name="category"     ),
   
]