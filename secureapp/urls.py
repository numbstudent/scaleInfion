from django.contrib.auth import views as auth_views
from secureapp import views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('change-password/', views.viewChangePassword, name='changepwd'),
]
