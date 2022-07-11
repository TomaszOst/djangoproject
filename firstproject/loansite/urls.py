from django.urls import path
from loansite.models import Client
from .views import HomeView
from . import views

app_name = 'loansite'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('customercreate/',views.client_form,name='client_form'),
    path('customercreate2/',views.clientinfo_form,name='clientinfo_form')
]

