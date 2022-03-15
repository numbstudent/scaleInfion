from mainApp.models import *
from mainApp.forms import *
from django.shortcuts import get_list_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import RestrictedError, Sum, Q, F
from django.db.models.functions import Coalesce
from django.contrib.auth.decorators import login_required
from django import template
from django.db import IntegrityError
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

loginpage = 'login'

@login_required(login_url=loginpage)
def index(request):
    return render(request, 'home.html')

@csrf_exempt
def BatchView(request):
    if request.is_ajax and request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)

    elif request.is_ajax and request.method == "GET":
        data = Product.objects.all()
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')


@csrf_exempt
def RegisterView(request, batchno=None):
    if request.is_ajax and request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(request.POST)
            code = request.POST.get('code')
            boxno = request.POST.get('boxno')
            productid = Product.objects.filter(code=code).first()
            boxexists = Register.objects.filter(product=productid, boxno=boxno).exists()
            if boxexists:
                return JsonResponse({"error": "Box sudah diinput. Hapus box terlebih dahulu."}, status=400)
            else:
                instance = form.save(commit=False)
                instance.product = productid
                instance.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)

    elif request.is_ajax and request.method == "GET":
        batchno = request.GET.get('batchno')
        if batchno:
            data = Register.objects.annotate(product_name=F('product__name'), logging_weighing=F('logging__weighing'))\
            .values('id', 'batchno', 'boxno', 'product_name', 'logging_weighing')\
            .filter(batchno=batchno).order_by('createdon')
        else:
            data = Register.objects.all().values()
        return JsonResponse(list(data), safe=False, status=200)

    elif request.method == "PUT":
        body = json.loads(request.body)
        registerid = body['registerid']
        batchno = body['batchno']
        obj = Register.objects.filter(id=registerid)
        print(obj)
        obj.delete()
        if batchno:
            data = Register.objects.annotate(product_name=F('product__name')).values('id', 'batchno', 'boxno', 'product_name')\
            .filter(batchno=batchno).order_by('createdon')
            print(data)
        else:
            data = Register.objects.all().values()
        return JsonResponse({list(data)}, status=200)
