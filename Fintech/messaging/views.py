from Crypto import Random
from Crypto.PublicKey import RSA
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
               return render(request, 'invalidSubmitMessage.html')
           title=request.POST.get('title')
           body = request.POST.get('body')
           encrypt=request.POST.get('encrypt')
           #return HttpResponse(encrypt)
           message_obj=private_message(sender=sender, recipient=recipient, title=title, body=body, encrypt=encrypt)
           #return render_to_response(request, 'makeMessages.html')
           #return render(request, 'makeMessages.html')
           #return HttpResponse(message_obj.encrypt)
           message_obj.save()
           return render(request, 'messageSuccessPage.html')



   else:
       form=NewMessageForm()

   #variables=RequestContext(request, {'form':form})
   return render(request, 'makeMessages.html', {'form':form})
   #return render_to_response( 'makeMessages.html', variables)


def invalid_submit_message(request):
    return render(request, 'invalidSubmitMessage.html')

def success(request):
    return render(request, 'messageSuccessPage.html')

def view_messages(request):
    allMessages= private_message.objects.all().filter(recipient=my_user(request))
    #allMessages=delete_message(request)
    key=key_generator()
    HttpResponse(str(get_private_key(key)))
    return render(request, 'viewMessages.html', {'allMessages': allMessages});

def delete_messages(request):
    allMessages = private_message.objects.all().filter(recipient=my_user(request))
    if request.method == 'POST':
        checks = request.POST.getlist('checks')
        for message in checks:
            # message=message.split(',')
            # user = User.objects.get(username=message[0])
            # sender=CustomUser.objects.all().filter(user=user)
            # allMessages.filter(recipient=my_user(request), sender=sender,  title=message[1], body=message[2]).delete()
            allMessages.filter(id=message).delete()
    return render(request, 'viewMessages.html', {'allMessages': allMessages});

#def encryption(message):



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

def key_generator():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    return key

def get_public_key(key):
    publicKey=key.publickey().exportKey(format='PEM', pkcs=1)
    return publicKey

def get_private_key(key):
    privateKey=key.exportKey(format='PEM', pkcs=1)
    return privateKey




