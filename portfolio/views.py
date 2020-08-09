from django.shortcuts import render
from .models import Skill
# Create your views here.
def home(request):
    skills=Skill.objects.all()
    return render(request,'portfolio/home.html',{'s':skills})