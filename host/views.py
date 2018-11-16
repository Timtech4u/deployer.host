from django.shortcuts import render
from django.http import HttpResponse
from .forms import DeployForm
from django.contrib.auth.decorators import login_required
import os

@login_required(login_url='/accounts/login/')
def new_deploy(request):
    if request.method == "POST":
        form = DeployForm(request.POST)
        if form.is_valid():
            form.save()
            ssh_key = form.cleaned_data.get('ssh_key')
            user = request.user
            os.system("{} {}".format("dokku apps:create", user))
            os.system("echo {} >> ~/{}.pub".format(ssh_key, user))
            os.system("dokku ssh-keys:add {} ~/{}.pub".format(user, user))
            return HttpResponse("SSH Key Added")
    else:
        form = DeployForm()
    return render(request, 'deploy.html', {'form': form})