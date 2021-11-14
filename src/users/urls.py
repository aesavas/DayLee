from django.urls import path
from .views import (
    register_profile_view,
)

urlpatterns = [
    path('register/', register_profile_view, name="register"),
]
