from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationsView, UserLoginView,
                         UserProfileView, UserRegistration)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistration.as_view(), name='register'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationsView.as_view(), name='email_verification'),
]
