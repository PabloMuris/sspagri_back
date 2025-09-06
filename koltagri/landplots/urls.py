from django.urls import path,re_path
from .views import CultivatesListView,CultivatesDetailView
urlpatterns = [
    path('locais',CultivatesListView.as_view(),name='locais'),
    path('locais/<int:pk>',CultivatesDetailView.as_view(),name='cultivates_detail'),
]
