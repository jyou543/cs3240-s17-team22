from django.shortcuts import render
from .models import Group
from .forms import MakeGroup


def submit_group(request):
    if request.method=='POST':
        form = MakeGroup(request.POST)
        if form.is_valid():
            group_name = request.POST.get('name','')
            group_members= request.POST.get('members','')
            group_obj = Group(name=group_name)
            #group_obj.save()
            for member in group_members:
                group_obj.members.add(member)
            return render(request, 'result.html')
    else:
        form= MakeGroup()

    return render(request, 'group.html', {'form': form});

def delete_member(group_obj,member):
    group_obj.entry_set.remove(member)

def add_member(group_obj, member):
    group_obj.entry_set.add(member)
