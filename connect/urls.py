from django.urls import path
from . import views

#app name is the name of app
app_name='connect'
urlpatterns = [
    path('',views.connects,name='connects'),
]

