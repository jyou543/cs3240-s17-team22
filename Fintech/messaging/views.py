from Crypto import Random
from Crypto.PublicKey import RSA
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from account.models import CustomUser
from django.contrib.auth.models import User
from groups.models import Group


from .models import private_message
from .forms import NewMessageForm
from .forms import NewGroupMessageForm


def messageHome(request):
    #return render_to_response('messageHome.html')
    return render(request, 'html5up/message_home.html')


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
               return render(request, 'html5up/invalid_submit.html')
           title=request.POST.get('title')
           body = request.POST.get('body')
           encrypt=request.POST.get('encrypt')
           message_obj=private_message(sender=sender, recipient=recipient, title=title, body=body, encrypt=encrypt)
           #return render_to_response(request, 'makeMessages.html')
           #return render(request, 'makeMessages.html')
           #return HttpResponse(message_obj.encrypt)
           if(not encrypt):
               message_obj.encrypt=False
           message_obj.save()
           if message_obj.encrypt:
               random_number = Random.new().read
               key = RSA.importKey(message_obj.recipient.publicKey)
               text = message_obj.body
               message_obj.body=str( key.encrypt(text.encode(), random_number)[0])
               message_obj.save()
           return render(request, 'html5up/message_success.html')



   else:
       form=NewMessageForm()

   #variables=RequestContext(request, {'form':form})
   return render(request, 'html5up/make_messages.html', {'form':form})
   #return render_to_response( 'makeMessages.html', variables)


def invalid_submit_message(request):
    return render(request, 'html5up/invalid_submit.html')

def success(request):
    return render(request, 'html5up/message_success.html')

def view_messages(request):
    allMessages= private_message.objects.all().filter(recipient=my_user(request))
    #allMessages=delete_message(request)
    key=key_generator()
    HttpResponse(str(get_private_key(key)))
    return render(request, 'html5up/view_messages.html', {'allMessages': allMessages});

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
    return render(request, 'html5up/view_messages.html', {'allMessages': allMessages});


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

# def enter_password(request):
#     allMessages = private_message.objects.all().filter(recipient=my_user(request), encrypt=True)
#     return render(request, 'enterPrivateKey.html', {'allMessages': allMessages});


def decrypt_messages(request):
    key = RSA.importKey(my_user(request).privateKey)
    allMessages=private_message.objects.all().filter(recipient=my_user(request), encrypt=True)
    for message in allMessages:
        text=eval(message.body)
        message.body=key.decrypt(text)
        message.encrypt=False
        message.save()
    allMessages = private_message.objects.all().filter(recipient=my_user(request))
    return render(request, 'html5up/view_messages.html', {'allMessages': allMessages});


def message_groups(request):
    if request.method == 'POST':
        form = NewGroupMessageForm(request.POST)
        if form.is_valid():
            sender = my_user(request)
            recipient = None
            allUsers = CustomUser.objects.all()
            groupName=request.POST.get('groupName')
            if(not Group.objects.all().filter(name=groupName)):
                return render(request, 'html5up/invalid_group.html')
            group=Group.objects.all().filter(name=groupName)[0]
            members=group.members.all().exclude(user=my_user(request).user)
            for member in members:
                recipient = member
                title = request.POST.get('title')
                body = request.POST.get('body')
                message_obj = private_message(sender=sender, recipient=recipient, title=title, body=body, encrypt=False)
                message_obj.save()
            return render(request, 'html5up/message_success.html')


    else:
        form = NewGroupMessageForm()

    return render(request, 'html5up/make_GroupMessages.html', {'form': form})

