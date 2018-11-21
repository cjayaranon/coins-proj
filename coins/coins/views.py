from django.conf import settings
from django.shortcuts import render
from django.views.generic import View

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {})

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html', {})
