from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('signup.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup_done(request):
    template = loader.get_template('signup_done.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signin(request):
    template = loader.get_template('signin.html')
    context = {}
    return HttpResponse(template.render(context, request))
