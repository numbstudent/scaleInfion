from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('batch', views.BatchView, name='batch'),
    path('register', views.RegisterView, name='register'),
    path('register/<str:batchno>', views.RegisterView, name='registerbatchno'),
]
