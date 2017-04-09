from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.core.context_processors import csrf
from .forms import SignupForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def signupform(request):
    #if form is submitted
    if request.method == 'POST':
        #will handle the request later
        form = SignupForm(request.POST)

        #checking the form is valid or not
        if form.is_valid():
            cd = form.cleaned_data
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            user_type = request.POST["user_type"]
            user = User.objects.create_user(username, email=email, password=password)
            user.save()
            uinfo = CustomUser()
            uinfo.user = user
            uinfo.user_type = user_type
            uinfo.save()
            return render(request, 'login.html')  # Redirect after POST

            # return render(request, 'result.html', {
            # 		'username': form.cleaned_data['username'],
            # 	})

    else:
        #creating a new form
        form = SignupForm()

    #returning form
    return render(request, 'signupform.html', {'form':form})

@login_required
def showdata(request):
    all_users = User.objects.all()
    return render(request, 'showdata.html', {'all_users': all_users, })


def log(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

@login_required
def loggedin(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'loggedin.html', c )


def invalid(request):
    return render(request, 'invalid.html')

@login_required
def loggedout(request):
    logout(request)
    return render(request, 'logout.html')