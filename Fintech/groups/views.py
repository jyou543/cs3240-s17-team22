from django.shortcuts import render
from .models import Group
from .forms import MakeGroup
from django.http import HttpResponse
from django.db.models import Q
from account.models import CustomUser
from django.contrib.auth.models import User

def groupHome(request):
    return render(request, 'html5up/groups.html')

def submit_groups(request):
    if request.method=='POST':
        current_user=my_user(request)
        #form = MakeGroup(request.POST, current_user=current_user)
        form = MakeGroup(request.POST)
        if form.is_valid():
            group_name = request.POST.get('name','')
            allGroups=Group.objects.all()
            if(allGroups.filter(name=group_name)):
                #return HttpResponse(allGroups)
                return render(request, 'invalidSubmitGroup.html')

            group_members= request.POST.getlist('members')
            group_obj = Group(name=group_name)
            group_obj.save()
            group_obj.members.add(my_user(request))
            for member in group_members:
                group_obj.members.add(member)
            #return HttpResponse(group_obj.members.all())
            #return HttpResponse("<h1>Success</h1>")
            return render(request, 'html5up/group_success.html')
    else:
        current_user=my_user(request).user
        form= MakeGroup(current_user=current_user)

    return render(request, 'html5up/makeGroups.html', {'form': form});

def invalid_submit_group(request):
    return render(request, 'invalidSubmitGroup.html')

def success(request):
    return render(request, 'html5up/group_success.html')

def view_groups(request):
    #allGroups= Group.objects.all().filter()
    #members=my_user(request)
    allGroups=Group.objects.all().filter(members=my_user(request))
    return render(request, 'html5up/viewGroups.html', {'allGroups': allGroups});


def leave_groups(request):
    allGroups = Group.objects.all()
    if request.method == 'POST':
        checks = request.POST.getlist('checks')
        for name in checks:
            # return HttpResponse("<h1>Success</h1>")
            allGroups.filter(name=name).delete()
    return render(request, 'html5up/viewGroups.html', {'allGroups': allGroups});

def view_groups_for_adding(request):
    allGroups=Group.objects.all().filter(members=my_user(request))
    return render(request, 'html5up/selectGroupToChange.html', {'allGroups': allGroups})

def select_members_to_add(request):
    notMembers = CustomUser.objects.all()
    groupName=None
    if request.method == 'POST':
        groupName=request.POST.get('groupName')
        group = Group.objects.all().filter(name=groupName)[0]
        #return HttpResponse(group)
        for member in group.members.all():
            notMembers=notMembers.exclude(user=member.user)
        #return HttpResponse(notMembers)
    return render(request, 'selectMembersToAdd.html',  {'groupName': groupName , 'notMembers': notMembers })

def add_members(request):
    if request.method=='POST':
        groupName=request.POST.get('groupName')
        newMembers=request.POST.getlist('checks')
        group=Group.objects.all().filter(name=groupName)[0]
        for username in newMembers:
            user = User.objects.get(username=username)
            custom_user=CustomUser.objects.all().filter(user=user)[0]
            group.members.add(custom_user)
        return render(request, 'html5up/addedMembers_success.html')


def my_user(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    #return username
    return CustomUser.objects.all().filter(user=user)[0]