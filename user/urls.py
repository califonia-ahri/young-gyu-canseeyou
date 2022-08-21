from django.urls import path
from .views import RegisterView, LoginView, ProfileView, SettingsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('settings/<int:pk>/', SettingsView.as_view(), name="setting"),
]