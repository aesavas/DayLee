from django.urls import path
from .views import (
    dashboard_view,
    create_diary_view,
    update_diary_view,
    delete_diary_view,
)

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create-diary/', create_diary_view, name='create-diary'),
    path('update-diary/<str:pk>', update_diary_view, name='update-diary'),
    path('delete-diary/<str:pk>', delete_diary_view, name='delete-diary'),
]