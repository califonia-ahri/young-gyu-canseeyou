from django.urls import path
from .views import RegisterView, LoginView, ProfileView, SettingView, StatisView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('home/', ProfileView.as_view(), name='home_view'),
    path("statis/", StatisView.as_view(), name="statis_view"),
    path('setting/', SettingView.as_view(), name='setting_view'),
]