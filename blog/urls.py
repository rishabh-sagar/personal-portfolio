
from django.urls import path
from . import views
#app name is the name of app
app_name='blog'
urlpatterns = [
    path('',views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
]