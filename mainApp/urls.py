from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='weighing'),
    path('product', views.ProductView, name='product'),
    path('scale', views.ScaleView, name='scale'),
    path('register', views.RegisterView, name='register'),
    path('register/<str:batchno>', views.RegisterView, name='registerbatchno'),

    path('master/product', views.viewProduct, name='viewproduct'),
    path('master/delete-product/<int:id>', views.deleteProduct, name='deleteproduct'),
    path('master/edit-product/<int:id>', views.editProduct, name='editproduct'),

    path('report/batch', views.reportBatch, name='reportbatch'),
]
