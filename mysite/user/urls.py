from django.urls import path
from .views import RegisterView, LoginView, ProfileView, SettingsView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_view'),
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile_view'),
    path('settings/<int:pk>/', SettingsView.as_view(), name='setting_view'),
    path('home/<int:pk>/', ProfileView.as_view(), name='home_view'),
    
]