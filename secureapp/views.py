from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db.models import RestrictedError
from .forms import *
from .decorators import allowed_users

# Create your views here.

loginpage = 'login'

def login(request):
    return render(request, 'login.html')


def viewChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('changepwd')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


@login_required(login_url=loginpage)
@allowed_users(allowed_roles=['administrator'])
def viewFeatureAccess(request):
    context = {}
    context['action'] = 'view'
    context['data'] = AccessList.objects.all()
    context['isvalid'] = 'yes'
    if request.method == "POST":
        form = FeatureAccessForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, '')
        else:
            context['isvalid'] = 'no'
    else:
        context['form'] = FeatureAccessForm()

    return render(request, 'registration/featureaccesslist.html', context=context)

@login_required(login_url=loginpage)
@allowed_users(allowed_roles=['administrator'])
def editFeatureAccess(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = AccessList.objects.get(id=id)
        form = FeatureAccessForm(instance=obj)
        context['data'] = AccessList.objects.all()
        context['form'] = form
    if request.method == 'POST':
        obj = AccessList.objects.get(id=id)
        form = FeatureAccessForm(request.POST, instance=obj)
        context['data'] = AccessList.objects.all()
        context['form'] = form
        if form.is_valid():
            form.save()
            context['message'] = "Data berhasil disimpan."
    return render(request, 'registration/featureaccesslist.html', context=context)

@login_required(login_url=loginpage)
@allowed_users(allowed_roles=['administrator'])
def viewUser(request):
    context = {}
    context['action'] = 'view'
    context['data'] = User.objects.all()
    context['isvalid'] = 'yes'
    if request.method == "POST":
        form = UserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
        else:
            context['isvalid'] = 'no'
    else:
        context['form'] = UserForm()

    return render(request, 'registration/userlist.html', context=context)


@login_required(login_url=loginpage)
@allowed_users(allowed_roles=['administrator'])
def deleteUser(request, id):
    obj = User.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('userlist')


@login_required(login_url=loginpage)
@allowed_users(allowed_roles=['administrator'])
def editUser(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = User.objects.get(id=id)
        form = UserForm(instance=obj)
        context['data'] = User.objects.all()
        context['form'] = form
    if request.method == 'POST':
        obj = User.objects.get(id=id)
        form = UserForm(request.POST, instance=obj)
        context['data'] = User.objects.all()
        context['form'] = form
        if form.is_valid():
            # obj.name = form.cleaned_data.get('name')
            # obj.code = form.cleaned_data.get('code')
            # obj.minweight = form.cleaned_data.get('minweight')
            # obj.maxweight = form.cleaned_data.get('maxweight')
            # obj.status = form.cleaned_data.get('status')
            # obj.save()
            form.save()
            context['message'] = "Data berhasil disimpan."
            # return redirect('userlist')
    return render(request, 'registration/userlist.html', context=context)

@allowed_users(allowed_roles=['administrator'])
def viewRegister(request):
    if request.POST == 'POST':
        form = UserForm()
        if form.is_valid():
            form.save()
            # user_group = Group.objects.get(name='my_group_name') 
            # user_group.user_set.add(your_user)
            messages.success(request, 'Account created successfully')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

@login_required(login_url=loginpage)
@allowed_users(allowed_roles=['administrator'])
def groupAdd(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        form = GroupAddForm()
        context['form'] = form
    if request.method == 'POST':
        obj = User.objects.get(id=id)
        form = GroupAddForm(request.POST)
        context['form'] = form
        if form.is_valid():
            group_id = form.cleaned_data.get('group').id
            my_group = Group.objects.get(id=group_id) 
            obj.groups.clear() #clear user from any group
            my_group.user_set.add(obj) #set user to group
            context['message'] = "Data berhasil disimpan."
            return redirect('userlist')
    return render(request, 'registration/groupadd.html', context=context)
