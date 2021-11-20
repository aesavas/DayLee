from django.urls import path
from .views import (
    register_profile_view,
    login_view,
    logout_view,
    create_master_password_view,
    #check_master_password_view,
    account_view,
    edit_account_view,
)

#app_name = "users"

urlpatterns = [
    path('register/', register_profile_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('create-master-password/', create_master_password_view, name='create-master-password'),
    #path('check-master-password/', check_master_password_view, name='check-master-password'),
    path('account/', account_view, name='account'),
    path('edit-account/', edit_account_view, name='edit-account'),
]
