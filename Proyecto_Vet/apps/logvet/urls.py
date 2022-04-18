from django.urls import path
from apps.logvet.views1 import *


urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/password/', ResetPasswordView.as_view(), name='reset_password'),
    path('logvet/change/password/<str:token>/', ChangePasswordView.as_view(), name='change_password'),
    path('new/user/', NewUserView.as_view(), name='new_user'),
]