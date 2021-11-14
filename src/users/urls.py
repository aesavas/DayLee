from django.urls import path
from .views import (
    register_profile_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path('register/', register_profile_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]
