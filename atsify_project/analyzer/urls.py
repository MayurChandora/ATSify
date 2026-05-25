from django.urls import path
from . import views

urlpatterns = [
    path('analyse/', views.analyse_view, name='analyse'),
    path('results/<uuid:analysis_id>/', views.results_view, name='results'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/delete/<uuid:analysis_id>/', views.delete_analysis_view, name='delete_analysis'),
]
