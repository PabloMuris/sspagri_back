from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.



class CultivatesView(TemplateView):
    template_name = 'sites.html'

class CultivatesDetailView(TemplateView):
    template_name = 'cultivate_detail.html'

class SiteDetailView(TemplateView):
    template_name = 'site/site_detail.html'