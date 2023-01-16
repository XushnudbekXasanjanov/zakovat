from django.conf import settings
from django.shortcuts import render,redirect
from .models import *


def Registration(request):
    if request.method == 'POST':
        cap_name = request.POST.get('cap_name')
        team_name = request.POST.get('team_name')
        username = request.POST.get('username')
        count = request.POST.get('count')
        if RegistrationTeam.objects.filter(team_name=team_name) and int(count) > 8 or int(count) < 2:
            return redirect('error')
        if int(count) > 8 or int(count) < 2:
            return redirect('count-error')
        if RegistrationTeam.objects.filter(team_name=team_name):
            return redirect('team-error')

        total = 0
        for i in RegistrationTeam.objects.all():
            total+=1

        if int(total) > 24:
            return redirect('full')
        else:
            RegistrationTeam.objects.create(fullname=cap_name, team_name=team_name, username=username, count=count)
            return redirect('success')


    return render(request,'index.html')

def FullTeamError(request):
    return render(request,'full.html')

def ErrorCount(request):
    return render(request,'count_error.html')

def ErrorTeam(request):
    return render(request,'team_error.html')

def ErrorAll(request):
    return render(request,'error.html')

def Success(request):
    return render(request,'success.html')

def Table(request):
    context = {
        'team':RegistrationTeam.objects.all()
    }
    return render(request,'table.html',context)
