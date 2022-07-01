from django.contrib.auth import views as auth_views
from secureapp import views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('change-password/', views.viewChangePassword, name='changepwd'),
    path('register', views.viewRegister, name='register'),

    path('userlist', views.viewUser, name='userlist'),
    path('delete-user/<int:id>',
         views.deleteUser, name='deleteuser'),
    path('edit-user/<int:id>', views.editUser, name='edituser'),
    path('group-add/<int:id>', views.groupAdd, name='groupadd'),
    path('featureaccess', views.viewFeatureAccess, name='featureacceess'),
    path('edit-featureaccess/<int:id>', views.editFeatureAccess, name='editfeatureacceess'),
]
