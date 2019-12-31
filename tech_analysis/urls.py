from django.urls import path
from . import views

app_name = "tech_analysis"
urlpatterns = [
    path('tech_analysis', views.analysis, name='Tech_Analysis'),
    path('search', views.results, name='Search_Results'),
]
