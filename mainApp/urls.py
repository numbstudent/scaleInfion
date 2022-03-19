from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='weighing'),
    path('batch', views.BatchView, name='batch'),
    path('scale', views.ScaleView, name='scale'),
    path('register', views.RegisterView, name='register'),
    path('register/<str:batchno>', views.RegisterView, name='registerbatchno'),
]
