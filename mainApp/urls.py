from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='weighing'),
    path('product', views.ProductView, name='product'),
    path('scale', views.ScaleView, name='scale'),
    path('weighingstate', views.viewWeighingState, name='weighingstate'),
    path('register', views.RegisterView, name='register'),
    path('register/<str:batchno>', views.RegisterView, name='registerbatchno'),

    path('master/product', views.viewProduct, name='viewproduct'),
    path('master/delete-product/<int:id>', views.deleteProduct, name='deleteproduct'),
    path('master/edit-product/<int:id>', views.editProduct, name='editproduct'),

    path('master/department', views.viewDepartment, name='viewdepartment'),
    path('master/delete-department/<int:id>', views.deleteDepartment, name='deletedepartment'),
    path('master/edit-department/<int:id>', views.editDepartment, name='editdepartment'),

    path('master/reporttitle', views.viewReportTitle, name='viewreporttitle'),
    path('master/delete-reporttitle/<int:id>', views.deleteReportTitle, name='deletereporttitle'),
    path('master/edit-reporttitle/<int:id>', views.editReportTitle, name='editreporttitle'),

    path('master/reportbody', views.viewReportBody, name='viewreportbody'),
    path('master/delete-reportbody/<int:id>', views.deleteReportBody, name='deletereportbody'),
    path('master/edit-reportbody/<int:id>', views.editReportBody, name='editreportbody'),

    path('report/batch', views.viewReportBatch, name='reportbatch'),
    path('report/batch/export', views.reportBatchCSV, name='reportbatchcsv'),
    path('report/batch/exportpdf', views.reportBatchPDF, name='reportbatchpdf'),

    path('uploadbatch', views.viewUploadBatch, name='viewuploadbatch'),
    path('delete-uploadbatch/<int:id>', views.deleteUploadBatch, name='deleteuploadbatch'),
]
