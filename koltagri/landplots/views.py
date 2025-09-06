from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

from .filters import SiteFilter
# Create your views here.

import django_filters
from.models import Site
from koltagri.core.models import Country


class CultivatesListView(ListView):
    model = Site
    template_name = 'sites.html'
    context_object_name = 'sites'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = SiteFilter(self.request.GET,queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Countries"] = Country.objects.all().values_list("name", flat=True)
        context["filter"] = self.filterset
        return context

class CultivatesDetailView(DetailView):
    model = Site
    template_name = 'site/site_detail.html'
    context_object_name = 'site'

