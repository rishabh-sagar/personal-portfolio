from django.urls import path
from . import views
#app name is the name of app
app_name='project'
urlpatterns = [
    path('',views.projects,name='projects'),
]