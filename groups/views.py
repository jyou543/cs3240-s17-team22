from django.shortcuts import render
from .models import Group
from .forms import MakeGroup
from django.http import HttpResponse
from django.db.models import Q
from account.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

@login_required
def groupHome(request):
    if request.user.customuser.is_SiteManager:
        return render(request, 'html5up/groups_sitemanager.html')
    else:
        return render(request, 'html5up/groups.html')

@login_required
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
                return render(request, 'html5up/invalid_submission.html')

            group_members= request.POST.getlist('members')
            group_obj = Group(name=group_name)
            group_obj.save()
            group_obj.members.add(my_user(request))
            for member in group_members:
                group_obj.members.add(member)
            #return HttpResponse(group_obj.members.all())
            #return HttpResponse("<h1>Success</h1>")
            if request.user.customuser.is_SiteManager:
                return render(request, 'html5up/group_success_SM.html')
            else:
                return render(request, 'html5up/group_success.html')
        else:
            current_user = my_user(request).user
            form = MakeGroup(current_user=current_user)
    else:
        current_user=my_user(request).user
        form= MakeGroup(current_user=current_user)

    return render(request, 'html5up/makeGroups.html', {'form': form});

@login_required
def invalid_submit_group(request):
    return render(request, 'html5up/invalid_submission.html')

@login_required
def success(request):
    return render(request, 'html5up/group_success.html')

@login_required
def view_groups(request):
    #allGroups= Group.objects.all().filter()
    #members=my_user(request)
    allGroups=Group.objects.all().filter(members=my_user(request))
    return render(request, 'html5up/viewGroups.html', {'allGroups': allGroups});


@login_required
def leave_groups(request):
    allGroups = Group.objects.all()
    #allGroups=Group.objects.all().filter(members=my_user(request))
    if request.method == 'POST':
        checks = request.POST.getlist('checks')
        for name in checks:
            # return HttpResponse("<h1>Success</h1>")
            allGroups.filter(name=name)[0].members.remove(my_user(request))
            if allGroups.filter(name=name)[0].members.count()==0:
                allGroups.filter(name=name).delete()
    return render(request, 'html5up/viewGroups.html', {'allGroups': allGroups.filter(members=my_user(request))});

@login_required
def view_groups_for_adding(request):
    allGroups=Group.objects.all().filter(members=my_user(request))
    return render(request, 'html5up/selectGroupToChange.html', {'allGroups': allGroups})

@login_required
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
        if len(notMembers) != 0:
            return render(request, 'html5up/selectMembersToAdd.html',  {'groupName': groupName , 'notMembers': notMembers })
        else:
            return render(request, 'html5up/group_full.html')

@login_required
def add_members(request):
    if request.method=='POST':
        groupName=request.POST.get('groupName')
        newMembers=request.POST.getlist('checks')
        group=Group.objects.all().filter(name=groupName)[0]
        for username in newMembers:
            user = User.objects.get(username=username)
            custom_user=CustomUser.objects.all().filter(user=user)[0]
            group.members.add(custom_user)
        if len(newMembers) != 0:
            return render(request, 'html5up/addedMembers_success.html')
        else:
            notMembers = CustomUser.objects.all()
            groupName=None
            if request.method == 'POST':
                groupName=request.POST.get('groupName')
                group = Group.objects.all().filter(name=groupName)[0]
                for member in group.members.all():
                    notMembers=notMembers.exclude(user=member.user)
                messages.error(request, 'No members selected')
            return render(request, 'html5up/selectMembersToAdd.html',  {'groupName': groupName , 'notMembers': notMembers })


def my_user(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    #return username
    return CustomUser.objects.all().filter(user=user)[0]

# SITE MANAGER GROUP FUNCTIONS

@login_required
def groupHomeSiteManager(request):
    return render(request, 'html5up/groups_sitemanager.html')

@login_required
def view_groups_site_manager(request):
    allGroups=Group.objects.all()
    if(not my_user(request).is_SiteManager):
        return HttpResponse("<h1>Forbidden</h1>")
    return render(request, 'html5up/viewGroups_SM.html', {'allGroups': allGroups});

@login_required
def delete_groups_site_manager(request):
    allGroups = Group.objects.all()
    if request.method == 'POST':
        checks = request.POST.getlist('checks')
        for name in checks:
            allGroups.filter(name=name).delete()
    return render(request, 'html5up/viewGroups_SM.html', {'allGroups': allGroups});

@login_required
def view_groups_for_adding_site_manager(request):
    allGroups=Group.objects.all()
    if (not my_user(request).is_SiteManager):
        return HttpResponse("<h1>Forbidden</h1>")
    return render(request, 'html5up/selectGroupToChange_SM.html', {'allGroups': allGroups})

@login_required
def select_members_to_add_site_manager(request):
    if (not my_user(request).is_SiteManager):
        return HttpResponse("<h1>Forbidden</h1>")
    #return HttpResponse("<h1>Success</h1>")
    notMembers = CustomUser.objects.all()
    groupName=None
    if request.method == 'POST':
        groupName=request.POST.get('groupName')
        group = Group.objects.all().filter(name=groupName)[0]
        for member in group.members.all():
            notMembers=notMembers.exclude(user=member.user)
    if len(notMembers) != 0:
        return render(request, 'html5up/selectMembersToAdd_SM.html',  {'groupName': groupName , 'notMembers': notMembers })
    else:
        return render(request, 'html5up/group_full_SM.html')

@login_required
def add_members_site_manager(request):
  if request.method=='POST':
        groupName=request.POST.get('groupName')
        newMembers=request.POST.getlist('checks')
        group=Group.objects.all().filter(name=groupName)[0]
        for username in newMembers:
            user = User.objects.get(username=username)
            custom_user=CustomUser.objects.all().filter(user=user)[0]
            group.members.add(custom_user)
        if len(newMembers) != 0:
            return render(request, 'html5up/addedMembers_success_SM.html')
        else:
            notMembers = CustomUser.objects.all()
            groupName=None
            if request.method == 'POST':
                groupName=request.POST.get('groupName')
                group = Group.objects.all().filter(name=groupName)[0]
                for member in group.members.all():
                    notMembers=notMembers.exclude(user=member.user)
                messages.error(request, 'No members selected')
            return render(request, 'html5up/selectMembersToAdd_SM.html',  {'groupName': groupName , 'notMembers': notMembers })


@login_required
def view_groups_for_deleting_site_manager(request):
    if (not my_user(request).is_SiteManager):
        return HttpResponse("<h1>Forbidden</h1>")
    allGroups=Group.objects.all()
    return render(request, 'html5up/selectGroupToChange_delete_SM.html', {'allGroups': allGroups})

@login_required
def select_members_to_delete_site_manager(request):
    #return HttpResponse("<h1>Success</h1>")
    groupName=None
    if request.method == 'POST':
        groupName=request.POST.get('groupName')
        group = Group.objects.all().filter(name=groupName)[0]
        members=group.members.all()
    if len(members) != 0:
        return render(request, 'html5up/selectMembersToDelete_SM.html',  {'groupName': groupName , 'members': members })
    else:
        return render(request, 'html5up/group_empty.html')

@login_required
def delete_members_site_manager(request):
    if request.method=='POST':
        groupName=request.POST.get('groupName')
        members=request.POST.getlist('checks')
        group=Group.objects.all().filter(name=groupName)[0]
        for username in members:
            user = User.objects.get(username=username)
            custom_user=CustomUser.objects.all().filter(user=user)[0]
            group.members.remove(custom_user)
        allGroups = Group.objects.all()
        if allGroups.filter(name=groupName)[0].members.count()==0:
            allGroups.filter(name=groupName).delete()
        return render(request, 'html5up/deletedMembersSuccess_SM.html')