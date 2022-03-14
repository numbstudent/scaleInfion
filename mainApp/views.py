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
def RegisterView(request):
    if request.is_ajax and request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            code = request.POST.get('code')
            productid = Product.objects.filter(code=code).first()
            print("productid")
            instance = form.save(commit=False)
            instance.product = productid
            instance.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)

    elif request.is_ajax and request.method == "GET":
        data = Register.objects.all()
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')
