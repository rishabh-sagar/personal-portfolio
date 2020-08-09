from django.shortcuts import render
from .models import Connect


# Create your views here.
def connects(request):
     connects=Connect.objects.all
     return render(request,'connect/connects.html',{'connects':connects})