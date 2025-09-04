from django.urls import path,re_path
from .views import CultivatesView,CultivatesDetailView,SiteDetailView
urlpatterns = [
    path('locais',CultivatesView.as_view(),name='locais'),
    path('detalhes',CultivatesDetailView.as_view(),name='cultivates_detail'),
    path("site/name",SiteDetailView.as_view(),name="site_detail")
]
