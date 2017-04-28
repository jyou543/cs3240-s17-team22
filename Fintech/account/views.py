from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.template.context_processors import csrf
from .forms import SignupForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib import messages
from messaging import views as messaging_views
import json
# Create your views here.


def signupform(request):
    #if form is submitted
    if request.method == 'POST':
        #will handle the request later
        form = SignupForm(request.POST)

        #checking the form is valid or not
        if form.is_valid():
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            user_type = request.POST["user_type"]
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username, email=email, password=password)
                user.save()
                uinfo = CustomUser()
                uinfo.user = user
                uinfo.user_type = user_type
                key = messaging_views.key_generator()
                publicKey = messaging_views.get_public_key(key)
                privateKey = messaging_views.get_private_key(key)
                uinfo.publicKey = publicKey
                uinfo.privateKey = privateKey
                uinfo.save()
                uinfo.save()
                return render(request, 'html5up/login.html')  # Redirect after POST
            else:
                messages.error(request, 'username is taken')
                return HttpResponseRedirect('/signup')
            # return render(request, 'result.html', {
            # 		'username': form.cleaned_data['username'],
            # 	})

    else:
        #creating a new form
        form = SignupForm()

    #returning form
    return render(request, 'html5up/signup.html', {'form':form})


@login_required
def showdata(request):
    all_users = User.objects.all()
    return render(request, 'showdata.html', {'all_users': all_users, })


def home(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'html5up/index.html', c)


def investor_info(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'html5up/investor_info.html', c)


def company_info(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'html5up/company_info.html', c)


def log(request):
    c = {}
    c.update(csrf(request))
    if not User.objects.filter(username="sm").exists():
       user = User.objects.create_user(username='sm', email='smEmail', password='sm')
       user.save()
       uinfo = CustomUser()
       uinfo.user = user
       uinfo.user_type = 'C'
       uinfo.is_SiteManager = True
       key = messaging_views.key_generator()
       publicKey = messaging_views.get_public_key(key)
       privateKey = messaging_views.get_private_key(key)
       uinfo.publicKey = publicKey
       uinfo.privateKey = privateKey
       uinfo.save()
    return render(request, 'html5up/login.html', c)


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/loggedin')
        else:
            return HttpResponseRedirect('/invalid')
    else:
        return HttpResponseRedirect('/invalid')


@login_required
def loggedin(request):
    c = {}
    c.update(csrf(request))
    if request.user.customuser.is_SiteManager:
        return render(request,'html5up/sitemanager.html', c)
    if request.user.customuser.user_type == 'I':
        return render(request, 'html5up/investor.html', c )
    elif request.user.customuser.user_type == 'C':
        return render(request, 'html5up/company.html', c )
    else:
        return render(request, 'html5up/investor.html', c)


def invalid(request):
    return render(request, 'html5up/invalid.html')


@login_required
def loggedout(request):
    logout(request)
    return render(request, 'html5up/loggedout.html')


@user_passes_test(lambda u: u.customuser.is_SiteManager)
def del_user(request):
    username = request.POST["username"]
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    # if user.DoesNotExist:
    #     messages.info(request, "User does not exist",extra_tags='safe')
    # else:
        user.delete()
        messages.info(request, "User deleted Successfully")
    else:
        messages.info(request, "User does not exist")
    return HttpResponseRedirect('/loggedin')


@user_passes_test(lambda u: u.customuser.is_SiteManager)
def sus_user(request):
    username = request.POST["username"]
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        if user.customuser.is_SiteManager:
            messages.info(request, "This user is a SiteManager and thus you cannot change his/her status")
        elif user.is_active:
            user.is_active = False
            user.save()
            messages.info(request, "User suspended Successfully")
        else:
            user.is_active = True
            user.save()
            messages.info(request, "The User is no longer suspended")
    else:
        messages.info(request, "User does not exist")
    return HttpResponseRedirect('/loggedin')

@user_passes_test(lambda u: u.customuser.is_SiteManager)
def make_sm(request):
    username = request.POST["username"]
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        if user.customuser.is_SiteManager:
            messages.info(request, "This user is already a Site Manager")
        else:
            user.customuser.is_SiteManager = True
            user.customuser.save()
            messages.info(request, "User is now a Site Manager")
    else:
        messages.info(request, "User does not exist")
    return HttpResponseRedirect('/loggedin')


def fdalogin(data):
    username = data.POST["username"]
    password = data.POST["password"]
    user = authenticate(username, password)
    if user is not None and user.is_active:
        print("in if")

        return HttpResponse("True")
    else:
        return HttpResponse("False")