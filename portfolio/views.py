
from django.shortcuts import render
from .models import Profile, Education, Skill, Project, Achievement

def home(request):
    context = {
        'profile': Profile.objects.first(),
        'education': Education.objects.all(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'achievements': Achievement.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)
