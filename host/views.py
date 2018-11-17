from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import DeployForm, SignUpForm
from .models import Deploy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import os

@login_required(login_url='/accounts/login/')
def new_deploy(request):
    deploy = get_object_or_404(Deploy, owner=request.user)
    if request.method == "POST":
        form = DeployForm(request.POST, instance=deploy)
        if form.is_valid():
            deploy = form.save(commit=False)
            deploy.owner = request.user
            deploy.save()
            ssh_key = form.cleaned_data.get('ssh_key')
            user = '{}'.format(request.user)
            os.system("whoami")
            os.system("pwd")
            os.system("{} {}".format("dokku apps:create", user))
            os.system("echo {} >> /home/host/{}.pub".format(ssh_key, user))
            os.system("sudo dokku ssh-keys:add {} /home/host/{}.pub".format(user, user))
            return render(request, 'success.html', {'user': user})
    else:
        form = DeployForm(instance=deploy)
    return render(request, 'deploy.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            uzernname = '{}'.format(request.user)
            uzer = get_object_or_404(User, username=uzernname)
            initial_deploy = Deploy(owner=uzer, ssh_key='')
            initial_deploy.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})