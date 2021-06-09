from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from accounts.forms import UserAdminCreationForm
from accounts.forms import UserAdminCreationForm

@login_required()
def register(request):
	form=UserAdminCreationForm()
	if request.method=='POST':
		form=UserAdminCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('register')
	context={
	'form':form
	}
	return rener(request,'register.html', context)