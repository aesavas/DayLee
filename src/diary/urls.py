from django.urls import path
from .views import (
    landing_page_view,
    dashboard_view,
)

urlpatterns = [
    path('', landing_page_view, name='landing-page'),
    path('dashboard/', dashboard_view, name='dashboard'),
]