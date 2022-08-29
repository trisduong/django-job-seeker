from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from job.models import Job
from userprofile.models import Userprofile

def frontpage(request):
    jobs = Job.objects.filter(status="active")

    return render(request, 'mysite/frontpage.html', {'jobs': jobs})

def awesomejobs(request):
    jobs = Job.objects.filter(status="OPEN")

    return render(request, 'mysite/frontpage.html', {'jobs': jobs})


def about(request):
    return render(request, 'mysite/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')

            if account_type == 'employer':
                userprofile = Userprofile.objects.create(user=user, is_employer=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)

            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'mysite/signup.html', {'form': form})