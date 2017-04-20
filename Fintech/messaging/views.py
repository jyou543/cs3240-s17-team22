from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from account.models import CustomUser
from django.contrib.auth.models import User


from .models import private_message
from .forms import NewMessageForm


def messageHome(request):
    #return render_to_response('messageHome.html')
    return render(request, 'messageHome.html')


def new_messages(request):
   if request.method == 'POST':
       user=my_user(request)
       form=NewMessageForm(request.POST)
       if form.is_valid():
           sender=my_user(request)
           #recipient = CustomUser.objects.all().filter('recipient')
           recipient= None
           allUsers=CustomUser.objects.all()
           for worker in allUsers:
               if worker.user.username==request.POST.get('recipient'):
                   recipient=worker
           if(recipient)==None :
               return HttpResponse("<h1>Failed</h1>")
           title=request.POST.get('title')
           body = request.POST.get('body')
           message_obj=private_message(sender=sender, recipient=recipient, title=title, body=body)
           #return render_to_response(request, 'makeMessages.html')
           #return render(request, 'makeMessages.html')
           message_obj.save()
           return HttpResponse("<h1>Success</h1>")



   else:
       form=NewMessageForm()

   #variables=RequestContext(request, {'form':form})
   return render(request, 'makeMessages.html', {'form':form})
   #return render_to_response( 'makeMessages.html', variables)


def view_messages(request):
    allMessages= private_message.objects.all().filter(recipient=my_user(request))
    #allMessages=delete_message(request)
    return render(request, 'viewMessages.html', {'allMessages': allMessages});

def delete_messages(request):
    allMessages = private_message.objects.all().filter(recipient=my_user(request))
    if request.method == 'POST':
        checks = request.POST.getlist('checks')
        for message in checks:
            # message=message.replace('[',"")
            # message=message.replace(']',"")
            message=message.split(',')
            #return HttpResponse(message[1])
            user = User.objects.get(username=message[0])
            sender=CustomUser.objects.all().filter(user=user)
            allMessages.filter(recipient=my_user(request), sender=sender,  title=message[1], body=message[2]).delete()
    return render(request, 'viewMessages.html', {'allMessages': allMessages});


def my_user(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    #return username
    return CustomUser.objects.all().filter(user=user)[0]

def check_valid_user(user):
    allUsers=CustomUser.objects.all()
    if(len(allUsers.all().filter(user=user.user))==0):
        return False
    else:
        return True



