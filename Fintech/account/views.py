from django.shortcuts import render
from .forms import SignupForm
from .models import User
# Create your views here.

def signupform(request):
	#if form is submitted
	if request.method == 'POST':
		#will handle the request later
		form = SignupForm(request.POST)

		#checking the form is valid or not
		if form.is_valid():
			username= request.POST.get('username','')
			password=request.POST.get('password','')
			user_obj = User(username=username, password=password)
			user_obj.save()
			return render(request, 'result.html', {
					'username': form.cleaned_data['username'],
				})

	else:
		#creating a new form
		form = SignupForm()

	#returning form
	return render(request, 'signupform.html', {'form':form});