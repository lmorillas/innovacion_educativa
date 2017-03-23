# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserEditForm


@login_required
def selecciona_talleres2(request):
	user = request.user
	if request.method == "POST":
		form = CustomUserEditForm(request, data=request.POST)
		if form.is_valid():
			# do something with the form
			return redirect("message_to_user_done")
	else:
		form = CustomUserEditForm(request)
	
	return render(request, "talleres.html", {'user': request.user})
	

@login_required
def selecciona_talleres(request):
    user = request.user
    form = CustomUserEditForm(request.POST or None, 
    	initial={'first_name':user.first_name, 
    	'last_name':user.last_name})
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return HttpResponseRedirect('%s'%(reverse('profile')))

    context = {
        "form": form,
        'user': user
    }
    return render(request, "talleres.html", context)


'''
@login_required
def profile(request):
    if request.method == 'POST':
        form = profileForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = profileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})

'''