from django.shortcuts import render
from . import models
from loansite.models import Client, ClientInfo
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from .forms import ClientForm, ClientForm2
# Create your views here.

class HomeView(TemplateView):
    template_name= "loansite/home.html"

def client_form(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ClientForm()
    return render(request,'loansite/client_form.html',{'form':form})

def clientinfo_form(request):
    if request.method == 'POST':
        form = ClientForm2(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/thanks')
    else:
        form= ClientForm2()
    return render(request,'loansite/clientinfo_form.html',{'form':form})

    

