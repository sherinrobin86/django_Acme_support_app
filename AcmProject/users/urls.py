from django.urls import path
from users.views import register, create_user

from django.contrib.auth import views as authentication_views
app_name ='users'

urlpatterns = [
     path('register/',register,name='register'),
     path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
      path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
     path('create/',create_user,name='createprofile'),
]
