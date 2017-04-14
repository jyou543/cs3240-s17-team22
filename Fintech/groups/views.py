from django.shortcuts import render
from .models import Group
from .forms import MakeGroup
from django.http import HttpResponse
from django.db.models import Q


def submit_groups(request):
    if request.method=='POST':
        current_user=my_user(request)
        #form = MakeGroup(request.POST, current_user)
        form = MakeGroup(request.POST)
        if form.is_valid():
            group_name = request.POST.get('name','')
            group_members= request.POST.get('members','')
            group_obj = Group(name=group_name)
            group_obj.save()
            for member in group_members:
                group_obj.members.add(member)
            return HttpResponse("<h1>Success</h1>")
            #return render(request, 'resultForMakeGroups.html')
    else:
        form= MakeGroup()

    return render(request, 'makeGroups.html', {'form': form});

def view_groups(request):
    allGroups= Group.objects.all().filter()
    #allGroups=Group.objects.all().filter(members=my_user(request))
    #return HttpResponse(len(allGroups))
    return render(request, 'viewGroups.html', {'allGroups': allGroups});


def leave_groups(request):
    allGroups = Group.objects.all()
    if request.method == 'POST':
        checks = request.POST.getlist('checks')
        for name in checks:
            # return HttpResponse("<h1>Success</h1>")
            allGroups.filter(name=name).delete()
    return render(request, 'viewGroups.html', {'allGroups': allGroups});

def add_member(group_obj, member):
    group_obj.entry_set.add(member)

def my_user(request):
        username = None
        if request.user.is_authenticated():
            username = request.user.username

def in_group():
    pass