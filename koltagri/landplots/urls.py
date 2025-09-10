from django.urls import path,re_path
from .views import CultivatesListView,SiteDetailView,CalendarDetailView
urlpatterns = [
    path('locais',CultivatesListView.as_view(),name='locais'),
    path('locais/<int:pk>',SiteDetailView.as_view(),name='cultivates_detail'),
    path('calendario/',CalendarDetailView.as_view(),name='calendar'),
]


