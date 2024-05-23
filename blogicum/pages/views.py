from django.views.generic.base import TemplateView
from django.shortcuts import render

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class RulesView(TemplateView):
    template_name = 'pages/rules.html'

def csrf_error(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)

def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)

def server_error(request):
    return render(request, 'pages/500.html', status=500)