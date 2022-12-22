from django.urls import path
from . import views

urlpatterns = [
    path('<str:s>', views.index)
]