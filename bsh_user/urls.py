from django.urls import path
from . import views


app_name = "bsh_user"
urlpatterns = [
    path('Results_Search_user', views.results, name='Results_Search_user'),
    path('Userpage', views.user_page, name='Userpage'),
    path('', views.analysis, name='AnalysisPage'),
]
