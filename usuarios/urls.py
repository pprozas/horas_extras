from django.urls import path, include
from usuarios.views import index, singup, login

urlpatterns = [
   path('', index, name = "index"),
   path('singup',singup, name = "singup"),
   path('login', login, name = "login" )
 
   
]