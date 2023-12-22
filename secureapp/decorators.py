from django.http import HttpResponse
from django.shortcuts import redirect
from secureapp.models import AccessList
import re, uuid
import os

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('registerqr')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Anda tidak diizinkan untuk melihat halaman ini. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>')
        return wrapper_func
    return decorator

def allowed_check(feature_alias):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            lines = ""
            # try:
            #     with open('/usr/share/okane/okane.txt') as f:
            #         lines = f.read().splitlines()[0]
            # except:
            #     print("An exception occurred")
            # # ma = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
            # ma = "ACCESS ALOWED"
            # if lines == ma:
            #     print("LOAD: OK")
            # else:
            #     try:
            #         filedir = os.path.abspath(__file__ + "/../../mainApp")
            #         os.remove(filedir+"/models.py")
            #         os.remove(filedir+"/apps.py")
            #         os.remove(filedir+"/forms.py")
            #     except:
            #         print("An exception occurred")
            #     print("LOAD: NOT OK")
            #     return HttpResponse('')
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].id

            allowed_group = AccessList.objects.filter(feature_alias=feature_alias).values_list('allowed_groups', flat=True)
            print(allowed_group)
            if group in allowed_group:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Anda tidak diizinkan untuk melihat halaman ini. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>')
        return wrapper_func
    return decorator


def allowed_check_function(feature_alias, request):
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].id

    print(group)

    allowed_group = AccessList.objects.filter(
        feature_alias=feature_alias).values_list('allowed_groups', flat=True)
    print(allowed_group)
    if group in allowed_group:
        return True
    else:
        return False
