import django_filters
from .models import Site
from koltagri.core.models import Country

class SiteFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    country = django_filters.ModelChoiceFilter(
        field_name="country",          
        queryset=Country.objects.all(), 
        label="País",                   
    )

    
    class Meta:
        model = Site
        fields = ['name', 'country']