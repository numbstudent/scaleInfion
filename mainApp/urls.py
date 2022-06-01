from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='weighing'),
    path('product', views.ProductView, name='product'),
    path('scale', views.ScaleView, name='scale'),
    # path('startbatch', views.viewWeighingState, name='startbatch'),
    # path('endbatch', views.viewEndBatch, name='endbatch'),
    path('registerqr', views.RegisterView, name='registerqr'),
    path('registerqr/<str:batchno>', views.RegisterView, name='registerbatchno'),
    path('history', views.viewHistory, name='history'),
    path('rejectbox', views.RejectBox, name='rejectbox'),


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

    path('weighingstate', views.viewWeighingState, name='viewweighingstate'),
    path('delete-weighingstate/<int:id>', views.deleteWeighingState, name='deleteweighingstate'),
    path('edit-weighingstate/<int:id>', views.editWeighingState, name='editweighingstate'),
    path('close-batch/<int:id>', views.closeWeighingState, name='closeweighingstate'),
    path('activate-batch/<int:id>/<str:status>', views.activateWeighingState, name='activateweighingstate'),
    path('batchno-history/<str:batchno>', views.viewBatchHistory, name='viewbatchhistory'),

    path('report/batch', views.viewReportBatch, name='reportbatch'),
    path('report/batch/export', views.reportBatchCSV, name='reportbatchcsv'),
    path('report/batch/exportpdf', views.reportBatchPDF, name='reportbatchpdf'),

    path('uploadbatch', views.viewUploadBatch, name='viewuploadbatch'),
    path('delete-uploadbatch/<int:id>', views.deleteUploadBatch, name='deleteuploadbatch'),
]
